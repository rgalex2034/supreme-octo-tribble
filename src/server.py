#!/usr/bin/python3
import ClientPool
import MessageRcv
import ClientRcv
import threading

IP = '127.0.0.1'
PORT = 5462

pool = ClientPool.ClientPool()
clrcv = ClientRcv.ClientRcv(IP, PORT, pool)
msgrcv = MessageRcv.MessageRcv(IP, PORT, pool)
clrcv.start()
msgrcv.start()
while True:
	msg = input()
	pool.write(msg)
