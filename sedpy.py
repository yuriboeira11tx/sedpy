#coding: utf-8
# Desenvolvedor: Derxs
# Version: 1.0
import wx, os

class ClasseJanela(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(ClasseJanela, self).__init__(*args, **kwargs)

		fonte_padrao = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

		self.dirname = ''
		self.filename = ''
		
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.control.SetBackgroundColour('#222222')
		self.control.SetForegroundColour('#ffffff')
		self.control.SetFont(fonte_padrao)

		self.CreateStatusBar() # Criando Statusbar

		# Setando valores para o Menubar
		arquivo_menu = wx.Menu()
		abrir_menu = arquivo_menu.Append(wx.ID_OPEN, '&Abrir', 'Abrir arquivo para editar')
		novo_menu = arquivo_menu.Append(wx.ID_NEW, '&Novo', 'Criar novo arquivo de texto')
		salvar_menu = arquivo_menu.Append(wx.ID_SAVE, '&Salvar', 'Salvar alterações no arquivo')
		sobre_menu = arquivo_menu.Append(wx.ID_ABOUT, '&Sobre', 'Informações do programa')

		# Menubar
		menu_bar = wx.MenuBar()
		menu_bar.Append(arquivo_menu, '&Arquivo')
		self.SetMenuBar(menu_bar)

		# Eventos
		self.Bind(wx.EVT_MENU, self.onAbrir, abrir_menu)
		self.Bind(wx.EVT_MENU, self.onNovo, novo_menu)
		self.Bind(wx.EVT_MENU, self.onSalvar, salvar_menu)
		self.Bind(wx.EVT_MENU, self.onArquivo, sobre_menu)
		
		# Setando configurações do Frame
		self.SetTitle('SEDPY')
		self.SetSize(700, 600)
		self.Centre()
		self.Show(True)

	def onArquivo(self, evento):
		# Caixa de diálogo de informação sobre o programa
		info_dlg = wx.MessageDialog(self, 'Um pequeno editor de texto. Desenvolvedor Derxs. Versão 1.0', 'Informação Simples Editor', wx.OK)
		info_dlg.ShowModal()
		info_dlg.Destroy()

	def onAbrir(self, evento):
		# Abrindo arquivo externo
		arquivo_externo_dlg = wx.FileDialog(self, 'Escolha um arquivo', self.dirname, '', '*.*', wx.FD_OPEN)

		if arquivo_externo_dlg.ShowModal() == wx.ID_OK:
			self.filename = arquivo_externo_dlg.GetFilename()
			self.dirname = arquivo_externo_dlg.GetDirectory()

			f = open(self.dirname+'/'+self.filename, 'r')

			self.control.SetValue(f.read())
			
			f.close()

			self.SetTitle('SEDPY - ' + self.filename)

		arquivo_externo_dlg.Destroy()

	def onSalvar(self, evento):
		# Salvando dados no arquivo
		if self.dirname != '':
			try:
				f = open(self.dirname+'/'+self.filename, 'w')
				f.write(self.control.GetValue())
				f.close()
				wx.MessageBox('Dados salvos com sucesso!', 'Sucesso', wx.ICON_INFORMATION)
			except:
				wx.MessageBox('Erro ao salvar dados', 'Erro inesperado', wx.ICON_ERROR)
		else:
			f = open('gerado-por-voce.txt', 'w')
			f.write(self.control.GetValue())
			f.close()
			
			self.SetTitle('SEDPY - gerado-por-voce.txt')

			wx.MessageBox('Dados salvos com sucesso!', 'Sucesso', wx.ICON_INFORMATION)

	def onNovo(self, evento):
		# Criando novo arquivo de texto
		arquivo_novo_dlg = wx.FileDialog(self, 'Criar novo arquivo', self.dirname, '', '*.*', wx.FD_SAVE)

		if arquivo_novo_dlg.ShowModal() == wx.ID_OK:
			self.filename = arquivo_novo_dlg.GetFilename()
			self.dirname = arquivo_novo_dlg.GetDirectory()

			f = open(self.filename, 'w')
			f.write(self.control.GetValue())
			f.close()

			self.SetTitle('SEDPY - ' + self.filename)

		arquivo_novo_dlg.Destroy()

def main():
	aplicacao = wx.App(False)
	ClasseJanela(None)
	aplicacao.MainLoop()

main()
