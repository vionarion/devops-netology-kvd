
1. Какого типа команда `cd`? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.

Встроенная команда

Встроенная, работает внутри сессии терминала, меняет указатель на текущую дерикторию внутренней функцией

Если использовать внешний вызов, то он будет работать со своим окружением, и менять текущий каталог внутри своего окружения, а на shell влиять не будет.  

2. Какая альтернатива без pipe команде `grep <some_string> <some_file> | wc -l`? `man grep` поможет в ответе на этот вопрос. Ознакомьтесь с [документом](http://www.smallo.ruhr.de/award.html) о других подобных некорректных вариантах использования pipe.

vagrant@vagrant:~$ cat test

1525312 sad123asxcz123sssxxx9 62

vagrant@vagrant:~$ grep 6 test -c

1

vagrant@vagrant:~$ grep 6 test | wc -l

1

vagrant@vagrant:~$ grep 7 test -c

0


3. Какой процесс с PID `1` является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?


vagrant@vagrant:~$ pstree -p

systemd(1)─┬─VBoxService(989)─┬─{VBoxService}(991)
           │                  ├─{VBoxService}(992)
           │                  ├─{VBoxService}(994)
           │                  ├─{VBoxService}(997)
           │                  ├─{VBoxService}(998)

4. Как будет выглядеть команда, которая перенаправит вывод stderr `ls` на другую сессию терминала?

Вывод сессии pts/0:

vagrant@vagrant:~$ ls -l \root 2>/dev/pts/1

vagrant@vagrant:~$ who

vagrant  pts/0        2022-02-07 15:01 (10.0.2.2)

vagrant  pts/1        2022-02-07 15:02 (10.0.2.2)

vagrant@vagrant:~$

Вывод в другой сессии pts/1:

vagrant@vagrant:~$ ls -l \root 2>/dev/pts/1

ls: cannot access 'root': No such file or directory

vagrant@vagrant:~$ ls: cannot access 'root': No such file or directory


5. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.

root@KVD-PC:~/Test# cat test

1525312
sad123asxcz123sssxxx9
62

root@KVD-PC:~/Test# cat test >test2

root@KVD-PC:~/Test# cat test2

1525312
sad123asxcz123sssxxx9
62

root@KVD-PC:~/Test#

6. Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?

Вывести полуится при использовании перенаправлении вывода:
    
~/vagrant$ tty
   
 /dev/pts/3
   
 ~/vagrant$ echo Hello from pts3 to tty3 >/dev/tty3
  
 ~/vagrant$ 

но наблюдать в графическом режиме не получиться, нужно переключиться в контекст TTY (Ctrl-Alt-F3 в моем случае):


Так же можно перенаправить контекст из tty в pty, этот вывод можно наблюдать уже будет, но после возврата в графический режим:
    
~/vagrant$ tty

/dev/pts/1

~/vagrant$ hello from tty3 to pts1


7. Выполните команду `bash 5>&1`. К чему она приведет? Что будет, если вы выполните `echo netology > /proc/$$/fd/5`? Почему так происходит?

bash 5>&1 - Создаст дескриптор с 5 и перенатправит его в stdout

echo netology > /proc/$$/fd/5 - выведет в дескриптор "5", который был пернеаправлен в stdout

если запустить echo netology > /proc/$$/fd/5 в новой сесии, получим ошибку, так как такого дескриптора нет на данный момент в текущей(новой) сессии

    
vagrant@vagrant:~$ echo netology > /proc/$$/fd/5

-bash: /proc/1096/fd/5: No such file or directory

vagrant@vagrant:~$ bash 5>&1

vagrant@vagrant:~$ echo netology > /proc.$$/fd/5

bash: /proc.1114/fd/5: No such file or directory

vagrant@vagrant:~$ echo netology > /proc/$$/fd/5

netology

vagrant@vagrant:~$ 

8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от `|` на stdin команды справа.
Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.

vagrant@vagrant:~$ ls -l /root 9>&2 2>&1 1>&9 |grep denied -c 

1

9>&2 - новый дескриптор перенаправили в stderr
2>&1 - stderr перенаправили в stdout 
1>&9 - stdout - перенаправили в в новый дескриптор

9. Что выведет команда `cat /proc/$$/environ`? Как еще можно получить аналогичный по содержанию вывод?

Переменные окружения

Так же есть варианты посмотреть:

printenv
env

10. Используя `man`, опишите что доступно по адресам `/proc/<PID>/cmdline`, `/proc/<PID>/exe`.

/proc/<PID>/cmdline - полный путь до исполняемого файла процесса [PID]
/proc/<PID>/exe - содержит ссылку до файла запущенного для процесса [PID], 
                        cat выведет содержимое запущенного файла, 
                        запуск этого файла,  запустит еще одну копию самого файла

11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью `/proc/cpuinfo`.

vagrant@vagrant:~$ grep sse /proc/cpuinfo
SSE 4.2

12. При открытии нового окна терминала и `vagrant ssh` создается новая сессия и выделяется pty. Это можно подтвердить командой `tty`, которая упоминалась в лекции 3.2. Однако:

     ```bash
     vagrant@netology1:~$ ssh localhost 'tty'
     not a tty
     ```

     Почитайте, почему так происходит, и как изменить поведение.

Единственное что с мог найти: то, что при подключении ожидается пользователь, а не другой процесс, и нет локального tty в данный момент. 

для запуска можно добавить -t - , и команда исполняется c принудительным созданием псевдотерминала


vagrant@vagrant:~$ ssh -t localhost 'tty'

vagrant@localhost's password:

/dev/pts/2

Connection to localhost closed.

vagrant@vagrant:~$

13. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись `reptyr`. Например, так можно перенести в `screen` процесс, который вы запустили по ошибке в обычной SSH-сессии.

При первых запусках ругался на права, 10-patrace.conf

после установки заначения  kernel.yama.ptrace_scope = 0

после чего процесс был перехвачен в screen, и продолжил работу после закрытия терминала. 

единственное в pstree процесс не отображался, точнее оботражался в виде процесса reptyr. не сразу сообразил что это то, что нужно 


15. `sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без `sudo` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию `echo string | sudo tee /root/new_file`. Узнайте что делает команда `tee` и почему в отличие от `sudo echo` команда с `sudo tee` будет работать.

команда tee делает вывод одновременно и в файл, указаный в качестве параметра, и в stdout, 

в данном примере команда получает вывод из stdin, перенаправленный через pipe от stdout команды echo

и так как команда запущена от sudo , соотвественно имеет права на запись в файл