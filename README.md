# Вопросы к SRE/DevOps на интервью

## Полезные сылки 
https://github.com/Tinkoff/career/blob/main/interview/README.md - IT собеседование в Тинькофф  
https://learnk8s.io/production-best-practices - Kubernetes best practice  
https://github.com/Swfuse/devops-interview/blob/main/interview.md - IT вопросы на 
https://www.opennet.ru/base/net/tcpdump_explore.txt.html
https://habr.com/ru/company/alexhost/blog/531170/ #tcpdump

## Мои вопросы
- В какую команду вы меня берете и на какой проект?  
- Какие задачи и какую функцию я буду выполнять?  
- Как у вас построен процесс повышения грейдов и пересмотра зарплат?  
-  На какой срок рассчитан этот проект?  
-  Какие карьерные перспективы могут меня ждать в вашей компании?  

### Kubernetes
**Контейнеры = Linux namespaces + crgoups + chroot + capabilities (Seccomp)**  
> (Seccomp (сокращение от secure computing) — механизм ядра Linuх, позволяющий процессам определять системные вызовы, которые они будут использовать. Если злоумышленник получит возможность выполнить произвольный код, seccomp не даст ему использовать системные вызовы, которые не были заранее объявлены.)

**Namespaces** отвечают за изоляцию процесса от других процессов
> https://selectel.ru/blog/mexanizmy-kontejnerizacii-namespaces/ - подробно
Пространство имён:
- Тип       Что изолирует:
- PID       PID процессов
- NETWORK   Сетевые устройства, сетки, порты и т.п.
- USER ID   Пользователей и групп
- MOUNT     Точки монтирования
- IPC       SystemV IPC, очереди сообщений POSIX
- UTS       Имя хоста и доменное имя NIS (информационная служба сети)

**Сgroups** (Control Groups) отвечают за изоляцию ресурсов  
  cgroups - это функция ядра Linux, которая ограничивает, учитывает и изолирует использование ресурсов (CPU, память, дисковый ввод/вывод, сеть) для набора процессов. 
  
- Ограничение ресурсов - можно определить сколько CPU или памяти будет использовать конкретный процесс
- Приоритезация – cgroups позволяют определить какой процесс в рамках одной `cgroup` более приоритетен для использования ресурсов
- Отчетность - лимиты ресурсов мониторятся и сообщаются на уровне `cgroup`
- Управление - можно изменить статус (frozen, stopped, restarted) всех процессов `cgroup` одной командой

### Dockerd полный путь старта контейнера
  создается процесс 
  делается срез файловой системы `chroot` (cgroups - нарезка ресурса, пробрасываются порты)
  создаются правила `iptables`

  1. Docker client contacted the Docker daemon.
  2. The Docker daemon pulled the "hello-world" image from the Docker Hub
  3. The Docker daemon created a new container from that image which runs the executable
  that produces the output you are currently reading.
  4. The Docker daemon streamed that output to the Docker client, which sent it to your
  terminal.

  Docker multi-stage builds:
    - Каждая инструкция FROM может использовать индивидуальный базовый образ и каждая из них начинает новую стадию сборки docker образа. 
      Но основное преимущество, что вы можете копировать необходимые артефакты из одной стадии в другую. То есть, из стейджинга в прод. 
      При многоэтапной сборке вы используете несколько операторов FROM в своем Dockerfile. Каждый оператор FROM может использовать разную базу, и каждый из них начинает новый этап сборки. 
      Вы можете выборочно копировать артефакты с одного этапа на другой, убирая все, что не нужно из конечного образа.

KUBERNETES:
  Kubectl apply manifest (что происходит после этой команды):
    https://github.com/jamiehannaford/what-happens-when-k8s/blob/master/README.md
  Kubelet:
    Validation and generators:
      - kubectl проведет валидацию на стороне клиента, не отправляя никаких запросов
      - kubectl формирует HTTP запрос, который будет отправлен на kube-apiserver
      - kubectl will also figure out whether other actions need to be triggered, such as recording the command (for rollouts or auditing), 
        or whether this command is just a "--dry-run"
    API groups and version negotiation:
      - k8s использует REST архитектуру и протокол OpenAPI. Другими словами, API у кубера не монолитное и имеет много отдельных ресурсов. 
        Собственно, выбирается нужный. Все ресурсы можно посмотреть командой kubectl api-resources
      - у k8s версионированный API, v1 - последняя версия ресурса
    Аутентификация пользователя/клиента:
      - Для аутентификации нужен kubeconfig
      - Аутентифицироваться в k8s можно по сертификату, Bearer токену, имени пользователя/паролю, через OpenID токен 
    ДАЛЬШЕ НАШ HTTP ЗАПРОС ЛЕТИТ НА KUBE-APISERVER
  Kube-apiserver:
    - Это главный интерфейс, через который клиенты и элементы контролплейна рулят нашим кластером. 
    Аутентификация:
      - Аписервер должен убедиться что запрашивающий является тем, за кого себя выдает. 
      В зависимости от опциий запуска будет проверка что:
        - HTTP-запрос закодирован ключом TLS, подписанным корневым сертификатом CA
        - проверит токен
        - проверит что учетные данные HTTP-запроса соответствуют его собственному локальному состоянию 
    Авторизация:
      - Например, через RBAC роль, настроенную админом. 
    Admission control (контроллеры допуска (последний бастион контроля перед сохранением объекта в etcd)):
      они бывают всякими, например, resource management, security, defaulting, and referential consistency
      examples of admission controllers resource management:
        - InitialResources устанавливает ограничения ресурсов по умолчанию для ресурсов контейнера на основе прошлого использования;
        - LimitRanger накладывает верхние границы на определенные ресурсы (не более 2 ГБ памяти, по умолчанию 512 МБ);
        - ResourceQuota подсчитывает и запрещает количество объектов (pods, rc, балансировщики нагрузки сервисов) или общее количество потребляемых ресурсов (cpu, память, диск) в пространстве имен.
        *после создания объекта, Kubernetes будет следить за существованием объекта. 
  ETCD:
    Здесь, наконец, kube-apiserver десериализует HTTP-запрос (inverse process of kubectl's generators) 
    и записывает наши объекты в БД, такие как
      - Deployment
      - Replicaset
      - Pod
  Initializers (инициализаторы): Ну на собесах фиг с ними 
  Kube-controller-manager:
    Контроллеры - это куча скриптов (участков кода) в одном бинарнике, которые асинхронно следят только за своей зоной ответственности. 
    - Deployments controller: 
      Создает репликасет, присоединяет к нему label selector и дает номер ревизии. 
    - ReplicaSets controller: 
      Проверяет состояние нового ReplicaSet, если видит несоответствие между тем, что есть, и тем, что требуется, пытается наплодить Pods, принадлежащих ReplicaSet. 
      При подъеме происходит магия SlowStartInitialBatchSize. То есть, при каждом успешном создании пода, новых подов поднимается в 2 раза больше. 
      Это сделано, чтобы не упороть KubeApiserver, если что-то пойдет не так. 
  Informers:
    Информер - сущность, позволяеющая контроллерам подписываться на события хранилища и легко составлять список интересующих их ресурсов. 
    Умеет, например, кешировать.   
  Scheduler:
    - Слушает события, шедулит поды на ноды в соответствии с запрошенными ресурсами/параметрами. 
  kubelet:
    Это агент, запущенный на каждой воркер ноде кластера k8s и отвечает, например, за управление жизненным циклом подов.
    Он обрабатывает всю логику перевода между абстракцией "Pod" и ее строительными блоками, контейнерами. 
    Он также обрабатывает всю сопутствующую логику, связанную с 
      - монтированием томов
      - протоколированием контейнеров
      - сборкой мусора и многими другими важными вещами
    Передает podSpec в CRI
  CRI (Docker, containerd (protocol buffers (it's like a faster JSON) and a gRPC API)): 
    - Cоздается Sandbox (песочница) включает в себя создание "pause" контейнера. 
    - "pause" контейнер паузы служит в качестве родительского для всех остальных контейнеров в Pod, 
    поскольку в нем размещается множество ресурсов уровня pod, 
    которые в конечном итоге будут использовать контейнеры рабочей нагрузки. 
    Эти "ресурсы" представляют собой пространства имен Linux (IPC, сеть, PID). 
  CNI:
    bridge/ipvlan/macvlan/sr-iov
    тут прокидывается виртуальный линк в под хоста, IP цепляется за "pause" контейнер, чтоб не потеряться при рестартах контейнера из-за ошибок, например.
  Inter-host networking:
    - overlay networking (Flannel, например)
    Для этого обычно используется концепция оверлейной сети, которая представляет собой способ динамической синхронизации маршрутов между несколькими узлами. 
    Одним из популярных поставщиков оверлейных сетей является Flannel. Когда он установлен, его основной задачей является обеспечение сети IPv4 третьего уровня между несколькими узлами в кластере. 
    Flannel не управляет тем, как контейнеры подключаются к узлу (это задача CNI remember), а скорее тем, как трафик передается между узлами. 
    Для этого он выбирает подсеть для узла и регистрирует ее в etcd. Затем он хранит локальное представление маршрутов кластера и инкапсулирует исходящие пакеты в UDP-датаграммы, гарантируя, что они дойдут до нужного узла. 
    Для получения дополнительной информации ознакомьтесь с документацией CoreOS.
  Container startup: 
    - Pull the image 
    - Create the container via CRI
    - Create network via CNI (всякие правила iptables)
    - post-start lifecycle хуки
    - Рединес пробы
    - Контейнер шуршит 

  Kubectl apply manifest (что происходит после этой команды) 2:
    валидация манифеста, kubectl идет в kubeapi
    (каждое событие api записывает в etcd)
    controller-manager на controlplane видит что надо что-то создать
    kube-scheduler подбирает подходящую ноду и говорит что нужно поднять под с таким-то pod-spec
    на ноде kubelet выполняет docker run или crictl run
  
    kube-proxy: через iptables (менеджит services)

  Контур управления:
    kube-apiserver:
    - представляет API Kubernetes
    - предназначен для горизонтального масштабирования, то есть развёртывание на несколько экземпляров.
    - На OpenAPI (OpenAPI - это cпецификация), на архитектуре REST
    etcd:
    - Распределённая и высоконадёжная БД в формате "ключ-значение", основное хранилище всех данных кластера в Kubernetes.
    kube-scheduler:
    - отслеживает созданные поды без привязанного узла и выбирает узел, на котором они должны работать.
    - согласно требованиям к ресурсам, ограничения, связанные с аппаратными/программными политиками, 
      принадлежности (affinity) и непринадлежности (anti-affinity) узлов/подов, местонахождения данных, предельных сроков. 
    kube-controller-manager: (куча контроллеров в одном бинаре)
    - Контроллер узла (Node Controller): уведомляет и реагирует на сбои узла.
    - Контроллер репликации (ReplicaSets): поддерживает правильное количество подов для каждого объекта ReplicaSets в системе.
    - Контроллер конечных точек (Endpoints Controller): заполняет объект конечных точек (Endpoints), то есть связывает сервисы (Services) и поды (Pods).
    - Контроллеры учетных записей и токенов (Account & Token Controllers): создают стандартные учетные записи и токены доступа API для новых пространств имен.
      Контроллер - это асинхронный скрипт, который работает над согласованием текущего состояния системы Kubernetes с желаемым состоянием.
      Полезно думать о кубелете как о контроллере! Он запрашивает Pods из kube-apiserver каждые 20 секунд (это настраивается), фильтруя те, чье NodeName совпадает с именем узла, на котором запущен kubelet. Получив этот список, он обнаруживает новые добавления, сравнивая их с собственным внутренним кэшем, и начинает синхронизировать состояние, если имеются какие-либо расхождения. 
  
  Компоненты узла:
    - kubelet: 
      следит за тем, чтобы контейнеры были запущены в поде.
      принимает набор PodSpecs, и гарантирует работоспособность и исправность определённых в них контейнеров. 
      Если pod создается, он регистрирует некоторые метрики запуска, в Prometheus для отслеживания pod.   
      У пода бывает несколько статусов: Pending, Running, Succeeded, Failed and Unknown
      Когда pod запускается впервые, kubelet вызывает команду удаленной процедуры RunPodSandbox (RPC). Песочница" - это термин CRI для описания набора контейнеров, который в языке Kubernetes, как вы догадались, является Pod.

    - kube-proxy:
      конфигурирует правила сети на узлах (iptables). При помощи них разрешаются сетевые подключения к вашим подам изнутри и снаружи кластера.
      kube-proxy использует уровень фильтрации пакетов в операционной системы, если он доступен. 
      В противном случае, kube-proxy сам обрабатывает передачу сетевого трафика.
  
  Как выбирается мастер в k8s: RAFT
  По какому протоколу API общается: OpenAPI (REST) HTTP/HTTPS
  Пробы:
    livenessProbe: Показывает, запущен ли контейнер
    readinessProbe: Указывает, готов ли контейнер отвечать на запросы
    startupProbe: Указывает, запущено ли приложение внутри контейнера
    *Нужно выбирать или livenessProbe + readinessProbe, или startupProbe.
    Если с пробами что-то не так, kubelet смотрит в restartPolicy, а они бывают трех видов - Always, OnFailure, and Never

  Сущности kubernetes:
    ReplicationController: старая, изначальная технология.
    ReplicaSets: появился matchLabels, вместо labels. 
      Но у него нет rolling-update, Вот по этому есть Deployment, он абстракция над ReplicaSets, добавляет rolling-update/rollback
    Services: связываются с подами по лейблам
      Kubernetes ServiceTypes allow you to specify what kind of Service you want.
      Type values and their behaviors are:
      - ClusterIP: Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. This is the default that is used if you don't explicitly specify a type for a Service. You can expose the service to the public with an Ingress or the Gateway API.
      - NodePort: Exposes the Service on each Node's IP at a static port (the NodePort). To make the node port available, Kubernetes sets up a cluster IP address, the same as if you had requested a Service of type: ClusterIP.
      - LoadBalancer: Exposes the Service externally using a cloud provider's load balancer.
      - ExternalName: Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up.
    StatefulSets:
    daemonset: гарантирует, что все (или некоторые по .spec.template.spec.{nodeSelector или affinity}) узлы запускают копию Pod. 
    operator:

    garbage collector вычищает по полю ownerReferences

  Сеть Kubernetes: 
    Pause контейнер держит netns
    У каждого пода свой уникальный IP
    На каждой ноде есть root netns. Основной сетевой интерфейс — eth0 — находится в этом root netns
    У каждого пода есть свой netns с виртуальным интерфейсом Ethernet, связывающим их с root netns (ip link). 
    Это виртуальный линк с одним концом в root netns и другим — в netns пода.
  
    Предположим, пакет отправляется из pod1 в pod2 внутри одной ноды:
    1. Он через eth0 покидает netns, принадлежащий pod1, и попадает в root netns через vethxxx.
    2. Попадает в cbr0, который выдаёт ему точку назначения с помощью ARP-запроса, спрашивающего «У кого такой IP-адрес?».
    3. vethyyy отвечает, что у него нужный IP — так мост узнаёт, куда переслать пакет.
    4. Пакет достигает vethyyy и, проходя виртуальный линк, попадает в netns, принадлежащий pod2.
    *поды, также, должны быть доступны из всех узлов (со всех нод).
    
    Взаимодействие между узлами (inter-node):
      Поды также должны быть доступны из всех узлов. И для Kubernetes вовсе не принципиально, как это реализовано. 
      Можно использовать L2 (ARP между узлами), 
      L3 (IP-маршрутизация между узлами — аналогично таблицам роутинга у облачных провайдеров), 
      оверлейные сети и даже почтовых голубей. 
      Каждому узлу назначается уникальный блок CIDR (диапазон IP-адресов) для IP-адресов, выдаваемых подам, 
      так что у каждого пода свой уникальный IP, не конфликтующий с подами других узлов. 

  Обычно существует 2 поля объекта: spec и status. 
    В поле spec указывается требуемое состояние (описание характеристик, которые должны быть у объекта).
    status описывает текущее состояние объекта

Процессы и треды (шаринг ресурсов):
  Поток — определенный способ выполнения процесса. Когда один поток изменяет ресурс процесса, это изменение сразу же становится видно другим потокам этого процесса.
  IP пода делится между всеми его контейнерами и является доступным (маршрутизируемым) для всех остальных подов.

Команды дебага: 
  lsof -p # deleted file 
  numactl --hardware, -H # список номеров нод, разделенных запятыми, или диапазонов A-B, или всех.
  perf:
    CPU:
      perf top
      perf stat ls -e
      perf 
  /usr/bin/perf_4.19 top -c 100
  strace
    strace -e trace=%network -p <PID> # смотреть сетeвые вызовы
    strace -f # посмотреть все дочерние процессы
    strace -e open -p 24106 # посмотреть все файлы, которые открывает процесс
    # запуск программ в пространстве имен, не разделенном с родительским.
  ulimit -n # Too many open files
  opensnoop # Следит за открытыми файлами
  dstat #сочетает в себе возможности iostat, vmstat, netstat и ifstat.
Докер:
  docker ps 

Ресурсы по ядру:
  syscalls https://man7.org/linux/man-pages/man2/syscalls.2.html
    The system call is the fundamental interface between an application and the Linux kernel.
Сетевые: 
  nslookup # DNS запросы
  tcpdump -A # как посмотреть пакеты, если трафик не шифрованный
  tcpdump -ni any net 10.232.232.0/31 -AvX 
    -A # Печать каждого пакета (за вычетом заголовка уровня соединения) в формате ASCII. Удобно для захвата веб-страниц.
    -v # verbose
    -X # Печать данных каждого пакета в шестнадцатеричном формате и ASCII. 

    tcpdump # можно проверить проходит ли пакет между хостами. Через wireshark можно посмотрреть кто виноват, клиент или сервер. 

  sudo ngrep -d any # сканить сетку

reset

Чаще всего, программа работает медленно из-за:
  CPU time
  Диска (много записей)
  Ожидания медленного сервера

Mastering the mentioned tools: (strace, tcpdump, netstat, lsof, ngrep, etc)

Методы мониторинга:
  Requests, Errors, Duration == RED Method

Ip ip over tcp или нет: Нет. TCP - L4, а IPIP и GRE-туннели — это туннели сетевого уровня (L3) модели OSI.
  IPIP и GRE-туннели — это туннели сетевого уровня (L3) модели OSI, при создании которых доступны IP-адреса обеих сторон. Они представляются в системе в виде интерфейсов GreX и IPIPX, и через них можно настраивать маршрутизацию (в том числе и default route) точно также, как и через любые другие интерфейсы. 
  Плюс ко всему для этих интерфейсов можно настроить уровень доступа security level — private, protected или public
  IPIP (IP over IP) один из самых простых в настройке туннелей (инкапсулирует только unicast IPv4-трафик). Его можно настроить как на UNIX/Linux-системе, так и на различных маршрутизаторах (например, Cisco).

fsnotify: Как ООМ выбирает кого убивать. 

UEFI # новый BIOS
Stage boot loader # синий экран загрузки, где можно задать синглмод

SIGHUP
  # Сигнал HUP (повесить трубку) примерно такой же, как SIGTERM с точки зрения резкости, но у него есть особая роль, поскольку он автоматически отправляется приложениям, работающим в терминале, когда пользователь отключается от этого терминала. Это сигнал номер 1. 
  The signals SIGKILL and SIGSTOP cannot be caught or ignored.
CGROUP

Восстановление etcd:
  Сжатие + дефрагментация + правильный мониторинг — основа обслуживания вашего кластера etcd.
  disaster recovery:
    --force-new-cluster

Вопросы с собесов:
  Отказоустойчивый, распределенный сервис DNS, например, на 5 зон

Вопросы от Барсукова:
  У вас есть ноутбук с линуксом, например убунтой, на рабочем столе запущен терминал,
  в нем вы запускаете curl https://example.com/расскажите, что произойдет

  Прострой отказоустойчивый сервис сокращения ссылок, например.

Свистелки:
  Argo cd (continuous delivery): декларативный инструмент для непрерывной доставки в Kubernetes по модели GitOps
  Terraform (IaC): управляет внешними ресурсами поставщиков услуг
    (например, облачная инфраструктура, инфраструктура частного облака, сетевые устройства, программное обеспечение как услуга и платформа как услуга)
  Istio Service Mesh:
    Istio идет как Control Plane, он состоит из трёх компонентов - Pilot, Mixer и Citadel
    envoy как sidecar у подов (Data Plane)
    # Istio перехватывает весь сетевой трафик и применяет к нему набор правил, вставляя в каждый pod умный прокси в виде sidecar-контейнера. Прокси, которые активируют все возможности, образуют собой Data Plane, и они могут динамически настраиваться с помощью Control Plane.
  ELK: (Elasticsearch, Logstash и Kibana)
    у нас ClickHouse, c kittenhouse - своей проксей + statsd 
  sr-iov: Single Root Input/Output Virtualization
  Calico:
    сетевая штука, через CRD поднимает networkpolicy, net
  Mesos:

  Apache Kafka: 
    Событие или сообщение — данные, которые поступают из одного сервиса, хранятся на узлах Kafka и читаются другими сервисами. Сообщение состоит из:
      Key — опциональный ключ, нужен для распределения сообщений по кластеру.
      Value — массив байт, бизнес-данные.
      Timestamp — текущее системное время, устанавливается отправителем или кластером во время обработки.
      Headers — пользовательские атрибуты key-value, которые прикрепляют к сообщению.

Менеджерские свистелки:
  Nexus: фреймворк - расширение классического скрама для крупных проектов с многокомандной разработкой. 

Consul


Вопросы без ответа: 
  Понимание BGP: это протокол динамической маршрутизации,
  Опыт построения контуров CI/CD

  range или to yaml (второе не мержит)
  Dependencies 
  Helmfile

  lvm 
  statefull

  services
  Как прокидывается файл из инит контейнера
  jagger
  openapi 
  gravitee
  
  
  vm ware - виртуализация, не интересно

LeetCode - уровень easy  https://leetcode.com/


dochouse
штурвал 
haiva
ipv6

DNS tcp udp 
git джит-компилятор

Consul
РЕД ОС



Terraform + Yandex Cloud
Пишут модули

Terragrand 

copy on write 
cap 
steal
dora 
dhcp 
acid 

Симметричное шифрование:
  Шифр Цезаря, RSA
Асимметричное шифрование:
  TLS, SSH

catacontainer
Безопасность:
  dlp системы

itil методология

Типы баз данных:
  Реляционные - SQL (мощная аналитика): 
    PostgreSQL
    MySQL
    MariaDB
    Oracle
    SQLite
  NoSQL - (Документные, похожие на Json)(Быстрый доступ к конкретной информации):
    MongoDB
    CouchDB
  NoSQL - key: value (Ключ: значение) 
    Redis 
    Memcached
  NoSQL - Временные ряды:
    Prometheus
    TimescaleDB
  NewSQL:
    ...
  Графовые:
    Dgraph

    TRIBE
    Воркер ноды 
    RHEL
    Пайпы

    Бюрократия
    #MTLS
    Кто делает SBERoS

    ПСИ - 


ISTIO%

У нас NGINX сайта перенаправлял запросы к одной из нескольких ферм энвоя, которая роутила запрос непосредственно в нужный k8s кластер. 
Я занимался мейнтененсом, расширением и траблшутингом фермы энвоев. 
