# use sudo
import MySQLdb as mysql
from rich.console import Console
console = Console()

db = mysql.connect(host = "localhost",user="root",passwd="1234",db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
data_dict = dict(res)	
console.print(f"Threads_connected : {data_dict['Threads_connected']}", style='bold green')
console.print(f"Threads_created : {data_dict['Threads_created']}", style = 'bold green')
console.print(f"Threads_running : {data_dict['Threads_running']}", style = 'bold green')
console.print(f"Uptime : {data_dict['Uptime']}", style = 'bold green')
console.print(f"Queries : {data_dict['Queries']}", style = 'bold green')
console.print(f"Max_used_connections : {data_dict['Max_used_connections']}", style = 'bold green')
console.print("------------------------------------PROCESS LIST TABLE--------------------------------",style = 'bold green')
cur.execute("select * from PROCESSLIST") 
res2 = cur.fetchall()
[console.print(f"USER ID -> {i[0]} | USER NAME -> {i[1]} | HOST NAME -> {i[2]} | DATABASE -> {i[3]} | COMMAND -> {i[4]} | TIME -> {i[5]} | STATE -> {i[6]} | INFO -> {i[7]}",style = 'bold blue') for i in res2 ]
db.close()