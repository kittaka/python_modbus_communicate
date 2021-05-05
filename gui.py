#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PySimpleGUI as sg
import modbus_client as mc
import modbustcp_server as ms
import importlib
importlib.reload(mc)
importlib.reload(ms)
#excelから設定値等を読み込み(将来対応)
#S=ba.excel_read(2,2)

start_address=0
sendlist=[0]*65535
#  セクション1 - オプションの設定と標準レイアウト
sg.theme('Dark Blue 3')

layout_tab1 = [
    [sg.Text("")],
    [sg.Text("ファンクション", size=(15, 1)),sg.Combo(("3","16(将来対応)"), default_value="3",size=(10, 1), key="-function_code-")],
    [sg.Text("開始レジスタ", size=(15, 1)), sg.InputText("123", key="start_register")],
    [sg.Text("レジスタ数", size=(15, 1)), sg.InputText("2", key="amount_of_registers")],
    [sg.Submit(button_text="クエリ実行",key="p1")]
]

layout_tab2 = [
    [sg.Text("")],
    [sg.Text("サーバー所持値", size=(15, 1)), sg.InputText("0",key="-server_value-")],
    [sg.Submit(button_text="サーバー起動",key="p2"),sg.Submit(button_text="サーバー停止",key="p3"),sg.Submit(button_text="サーバーの所持値変更",key="p4")],
]

layout = [
    [sg.Text("設定入力　※すべて10進数で入力")],
    [sg.Text("サーバーIP", size=(15, 1)), sg.InputText("127.0.0.1",key="-server_IP-")],
    [sg.Text("サーバーポート", size=(15, 1)), sg.InputText("502",key="-server_port-")],
    [sg.TabGroup([[sg.Tab('クライアント操作', layout_tab1), sg.Tab('サーバー操作', layout_tab2)]])],
    [sg.Text("動作ログ")],
    [sg.Output(size=(100, 15), key='-MULTILINE-')],
    [sg.Button('ログをコピー'), sg.Button('ログをクリア')]
]    

# セクション 2 - ウィンドウの生成
window = sg.Window("ModbusTCP通信クライアント", layout)

# セクション 3 - イベントループ
while True:
    event, values = window.read()

    if event is None:
        print("exit")
        break

    if event == "p1":
        mc.modbus_com(values["-server_IP-"],values["-server_port-"],values["-function_code-"],values["start_register"],values["amount_of_registers"])
        #print("クエリ送信完了")
    if event == "p2":
        ms.server_start(values["-server_IP-"],values["-server_port-"])
        print("サーバー起動")
    if event == "p3":
        ms.server_stop(values["-server_IP-"],values["-server_port-"])
        print("サーバー停止")
    if event == "p4":
        for i in range(len(sendlist)):
            sendlist[i]=int(values["-server_value-"])
        ms.server_wordset(start_address,sendlist)
        print("サーバー所持値変更")
    if event == 'ログをクリア':
        print('ログをクリア')
        window.FindElement('-MULTILINE-').Update('')
    if event == 'ログをコピー':
        window.FindElement('-MULTILINE-').Widget.clipboard_append(window.find_element('-MULTILINE-').Get())
        sg.popup('ログをコピーしました')
        
        
# セクション 4 - ウィンドウの破棄と終了
window.close()


# In[ ]:





# In[ ]:




