from typing import final
import PySimpleGUI as sg
import os
from event import Event
from datetime import datetime
# Create options for the dropdown tab


class TelaAgenda:

    def __init__(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Nomeio o Trabalho:'), sg.Input(
                key='-InputNome-', size=(20, 1), pad=(15, 3))],
            [sg.Text('Marque o prazo do seu trabalho:'), sg.Input(
                key='-Calendar-', size=(9, 1), pad=(19, 3))],
            [sg.CalendarButton('Calendário', close_when_date_chosen=True,  target='-Calendar-',
                               location=(0, 0), no_titlebar=False, format='%d-%m-%Y')],
            [sg.Text('Tempo estimado para conclusão em dias:'),
             sg.Input(key='-Estimativa-', size=(3, 1))],
            [sg.Button('Adicionar'), sg.Button('Excluir')],
            [sg.Exit('Concluir')]
        ]

        self.window = sg.Window('Agenda de Entregas', layout, finalize=True)
        self.trabalhos = []
        # list of events

    def encontra_Trabalhos(self):
        self.delecoes = []
        i = 0
        for nomes in self.trabalhos:
            if self.trabalhos != []:
                self.delecoes.append(self.trabalhos[i].get_name())
            i = i+1

    def deleta_Trabalhos(self, deletado):
        i = 0
        for cnt in self.trabalhos:
            if self.trabalhos[i].get_name() == deletado:
                self.trabalhos.pop(i)
            i = i+1

    def janela_Secundaria(self):

        self.encontra_Trabalhos()

        layoutExclui = [
            [sg.Text("Trabalho a ser excluido:"), sg.Combo(
                self.delecoes, size=(20, 5), enable_events=True, key='-BtnExcluir-')],
            [sg.Exit('Concluir'), sg.Exit('Cancelar')]
        ]

        self.windowBtn = sg.Window('nova Janela', layoutExclui, finalize=True)
        self.windowBtn['-BtnExcluir-'].bind('<KeyRelease>', 'KEY DOWN')

        while True:

            self.eventBtn, self.valuesBtn = self.windowBtn.read()

            if self.eventBtn in (sg.WIN_CLOSED, 'Cancelar'):
                break
            elif self.eventBtn == 'Concluir':
                self.deletado = self.valuesBtn['-BtnExcluir-']
                self.deleta_Trabalhos(self.deletado)
                sg.popup(
                        'Trabalho excluido com sucesso!')
                break
            elif self.eventBtn == "-BtnExcluir-KEY DOWN":
                self.windowBtn['-BtnExcluir-'].Widget.event_generate('<Down>')

        self.windowBtn.close()

    def desenhar_Janela(self):
        
        keys_to_clear = ['-InputNome-', '-Calendar-', '-Estimativa-']
        while True:
            # print(self.values['-Calendar-'])
            # print(type(self.values['-Calendar-']))

            self.event, self.values = self.window.read()

            if self.event in (sg.WIN_CLOSED, 'Concluir'):
                break
            elif self.event == 'Adicionar':
                # parse date in YYYY-MM-DD format to datetime object
                deadline = self.values['-Calendar-']
                deadline = datetime.strptime(deadline, '%d-%m-%Y')
                event = Event(deadline=deadline, duration=int(
                    self.values['-Estimativa-']), name=self.values['-InputNome-'])
                self.trabalhos.append(event)
                sg.popup(
                    'Trabalho Adicionado!')
                for keys in keys_to_clear:
                    self.window[keys]('')
            elif self.event == 'Excluir':
                print(self.trabalhos)
                if self.trabalhos == []:
                    sg.popup(
                        'Nenhum Trabalho foi adicionado')
                else:
                    self.janela_Secundaria()

        self.window.close()

    def start():
        UI = TelaAgenda()
        UI.desenhar_Janela()
        print(UI.trabalhos)
        return UI.trabalhos
