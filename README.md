# Вопросы к SRE/DevOps на интервью
1. [Полезные сылки](#Полезные-сылки)
2. [Мои вопросы](#Мои-вопросы-к-интервьюеру)
3. [Контейнеризация](#Контейнеризация)
4. [DevOps практики](#DevOps-практики)
5. [Dockerd полный путь старта контейнера](#Dockerd-полный-путь-старта-контейнера)
6. [Docker multi-stage builds](#Docker-multi-stage-builds)
7. [Kubectl apply manifest - что происходит после этой команды (коротко)?](https://github.com/Rakhmankulov/Interviews/blob/main/README.md#kubectl-apply-manifest---%D1%87%D1%82%D0%BE-%D0%BF%D1%80%D0%BE%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%B8%D1%82-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D1%8D%D1%82%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%BE)
8. [Kubectl apply manifest - что происходит после этой команды (развернуто)?](https://github.com/Rakhmankulov/Interviews/blob/main/README.md#kubectl-apply-manifest---%D1%87%D1%82%D0%BE-%D0%BF%D1%80%D0%BE%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%B8%D1%82-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D1%8D%D1%82%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D0%BD%D1%83%D1%82%D0%BE)
9. [Компоненты контура управления Kubernetes](#Компоненты-контура-управления-Kubernetes)
10. [Компоненты worker-ноды Kubernetes](#Компоненты-worker-ноды-Kubernetes)
11. [Общие вопросы по Kubernetes](#Общие-вопросы-по-Kubernetes)
12. [Сущности Kubernetes](#Сущности-Kubernetes)
13. [Сеть в Kubernetes](#Сеть-в-Kubernetes)
14. [Команды дебага Linux](#Команды-дебага-Linux)
15. [Общие вопросы с собесов](#Общие-вопросы-с-собесов)
16. [Шифрование](#Шифрование)
17. [Типы баз данных](#Типы-баз-данных)
18. [Свистелки (Удобные инструменты DevOps)](#Свистелки)
19. [Менеджерские свистелки (Снова удобные инструменты)](#Менеджерские-свистелки)
20. [Вопросы без ответа](#Вопросы-без-ответа)

## Полезные сылки 
https://github.com/Tinkoff/career/blob/main/interview/README.md - IT собеседование в Тинькофф  
https://learnk8s.io/production-best-practices - Kubernetes best practice  
https://github.com/Swfuse/devops-interview/blob/main/interview.md - IT вопросы на собесе  
https://www.opennet.ru/base/net/tcpdump_explore.txt.html - tcpdump  
https://habr.com/ru/company/alexhost/blog/531170/ - tcpdump  

## Мои вопросы к интервьюеру
- Эта позиция, на которую вы меня собеседуете - новая, или я заменю старого сотрудника? Чем не подошел старый сотрудник? 
- В какую команду вы меня берете и на какой проект?  
- Какие задачи решать и какую функцию я буду выполнять?  
- Как у вас построен процесс повышения грейдов и пересмотра зарплат?  
- На какой срок рассчитан этот проект?  
- Какие карьерные перспективы могут меня ждать в вашей компании?  

# Ответы на вопросы
## Контейнеризация
`Контейнеры` = Linux namespaces + crgoups + chroot + capabilities (Seccomp) 
> (Seccomp (сокращение от secure computing) — механизм ядра Linuх, позволяющий процессам определять системные вызовы, которые они будут использовать. Если злоумышленник получит возможность выполнить произвольный код, seccomp не даст ему использовать системные вызовы, которые не были заранее объявлены.)

`Namespaces` отвечают за изоляцию процесса от других процессов  
[Механизмы контейнеризации: namespaces](https://selectel.ru/blog/mexanizmy-kontejnerizacii-namespaces/)    

Пространство имён:  
  | Тип      | Что изолирует |
  |-|-|
  | PID      | PID процессов |
  | NETWORK  | Сетевые устройства, сетки, порты и т.п. |
  | USER ID  | Пользователей и групп |
  | MOUNT    | Точки монтирования |
  | IPC      | SystemV IPC, очереди сообщений POSIX |  

`Сgroups` (Control Groups) отвечают за изоляцию ресурсов  
  cgroups - это функция ядра Linux, которая ограничивает, учитывает и изолирует использование ресурсов (CPU, память, дисковый ввод/вывод, сеть) для набора процессов. 
  
- Ограничение ресурсов - можно определить сколько CPU или памяти будет использовать конкретный процесс
- Приоритезация – cgroups позволяют определить какой процесс в рамках одной `cgroup` более приоритетен для использования ресурсов
- Отчетность - лимиты ресурсов мониторятся и сообщаются на уровне `cgroup`
- Управление - можно изменить статус (frozen, stopped, restarted) всех процессов `cgroup` одной командой  

`Chroot` — операция изменения корневого каталога диска для запущенного процесса и его дочерних процессов. Программа, запущенная в таком окружении, не может получить доступ к файлам вне нового корневого каталога. Это измененное окружение называется chroot jail.  

## DevOps практики  
#### Этапы CI/CD  
  `CI` - Непрерывная интеграция:  
    1. План  
    2. Код  
    3. Сборка  
    4. Тест  
  `CD` - Непрерывная доставка:  
    1. Тест  
    2. Релиз  
    3. Развертывание  
    4. Поддержка и мониторинг  
    ![DevOps Practics](https://github.com/Rakhmankulov/Interviews/blob/main/images/DevOpsPractics.png)

## Dockerd полный путь старта контейнера
[50 вопросов по Docker, которые задают на собеседованиях, и ответы на них](https://habr.com/ru/companies/slurm/articles/528206/)  

1. Docker client связывается с Docker daemon  
2. Docker daemon скачивает образ `"hello-world"` с Docker Hub  
3. Docker daemon создает новый контейнер из этого образа в котором запускает исполняемый файл, который производит вывод фразы `"hello-world"` 
4. Docker daemon передает этот вывод Docker клиенту, который выводит его фразу `"hello-world"` ваш терминал  

## Docker multi-stage builds
При многоэтапной сборке вы используете несколько операторов `FROM` в вашем `Dockerfile`. Каждая инструкция `FROM` использует произвольный базовый образ и начинает новый этап сборки. Вы можете выборочно копировать артефакты с одного этапа на другой, оставляя только то, что вам необходимо в конечном образе. Чтобы показать, как это работает, давайте адаптируем Dockerfile из предыдущего раздела для этого процесса.  

Dockerfile:
```bash
FROM golang:1.7.3
WORKDIR /go/src/github.com/alexellis/href-counter/
RUN go get -d -v golang.org/x/net/html  
COPY app.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/alexellis/href-counter/app .
CMD ["./app"]
```  

Теперь вам нужен только один `Dockerfile`. Более того, вам больше не нужен и отдельный скрипт сборки. Просто запустите сборку образа привычной командой.

```bash
docker build -t avmaksimov/href-counter:latest .
```  

В итоге, вы получаете крошечный образ. Фишка в том, что вам не нужно извлекать промежуточные артефакты на вашу локальную систему.  

Как это работает? Вторая команда `FROM` начинает новый этап сборки с базового образа `alpine:latest`. Инструкция `COPY --from=0` копирует артефакты с предыдущего этапа сборки на текущий этап, благодаря чему необходимые для сборки Go SDK и любые промежуточные артефакты не сохраняются в конечном образе. 

## Kubernetes
#### Kubectl apply manifest - что происходит после этой команды (коротко)?  
  - валидация манифеста на стороне `kubelet` и аутентификация на воркер-ноде;  
  - `kubectl` идет в `kube-apiserver` на мастер-ноду, проходя при этом аутентификацию и авторизацию;  
  - каждое событие `kube-apiserver` записывает в `etcd`;  
  - `controller-manager` видит что надо что-то создать;  
  - `kube-scheduler` подбирает подходящую ноду и говорит что нужно поднять под с нужным `pod-spec`;   
  - на воркер-ноде `kubelet` выполняет `docker run` или `crictl run`  
  - `CRI` поднимает нужный нам `Pod` и следит за тем чтоб он исправно шуршал
    
#### Kubectl apply manifest - что происходит после этой команды (развернуто)?
[Источник](https://github.com/jamiehannaford/what-happens-when-k8s/blob/master/README.md)  

**1. Дейстия внутри Kubelet** 
  - Валидация и генераторы:  
    - `kubectl` проводит валидацию на стороне клиента, не отправляя никаких запросов  
    - `kubectl` формирует `HTTP` запрос, который будет отправлен на `kube-apiserver`
    - `kubectl` также выяснит, нужны ли какие-либо действия, например, запись команды (для роллоута или аудита), или же эта команда просто "--dry-run".  
  - API groups and version negotiation:
    - k8s использует REST архитектуру и протокол OpenAPI. Другими словами, API у кубера не монолитное и имеет много отдельных ресурсов. Собственно, выбирается нужный. Все ресурсы можно посмотреть командой `kubectl api-resources`  
    - у `k8s` версионированный API, v1 - последняя версия ресурса  
  - Аутентификация пользователя/клиента:  
    - Для аутентификации нужен `kubeconfig`  
    - Аутентифицироваться в k8s можно по сертификату, Bearer токену, имени пользователя/паролю, через OpenID токен   

**2. HTTP запрос отправляется на Kube-apiserver**  
`Kube-apiserver` - это главный интерфейс, через который клиенты и элементы контролплейна рулят нашим кластером.  
  - Аутентификация:  
    - `Kube-apiserver` должен убедиться, что запрашивающий является тем, за кого себя выдает. В зависимости от опциий запуска будет проверка что **HTTP-запрос закодирован ключом TLS**, подписанным корневым сертификатом CA, **или проверит токен**, или проверит что **учетные данные HTTP-запроса** соответствуют его собственному локальному состоянию.  
  - Авторизация:  
    - Например, через `RBAC` роль, настроенную админом.  
  - `Admission control`: (контроллеры допуска (последний бастион контроля перед сохранением объекта в `etcd`)):  
    > они бывают всякими, например, resource management, security, defaulting, and referential consistency examples of admission controllers resource management.    
    - `InitialResources` устанавливает ограничения ресурсов по умолчанию для ресурсов контейнера на основе прошлого использования;  
    - `LimitRanger` накладывает верхние границы на определенные ресурсы (не более 2 ГБ памяти, по умолчанию 512 МБ);  
    - `ResourceQuota` подсчитывает и запрещает количество объектов (pods, rc, балансировщики нагрузки сервисов) или общее количество потребляемых ресурсов (cpu, память, диск) в пространстве имен.

**3. После создания объекта, Kubernetes будет следить за существованием объекта**  
  - `ETCD`:  
    Здесь, наконец, `kube-apiserver` десериализует HTTP-запрос (inverse process of kubectl's generators) и записывает наши объекты в БД, такие как:  
      - Deployment
      - Replicaset
      - Pod
  > `Initializers` (инициализаторы): Ну на собесах фиг с ними

  - `Kube-controller-manager`:  
`Контроллеры` - это куча скриптов (участков кода) в одном бинарнике, которые асинхронно следят только за своей зоной ответственности.  
    - `Deployments controller` cоздает репликасет, присоединяет к нему label selector и дает номер ревизии.  
    - `ReplicaSets controller` проверяет состояние нового `ReplicaSet`, если видит несоответствие между тем, что есть, и тем, что требуется, пытается наплодить `Pods`, принадлежащих `ReplicaSet`.  
      > При подъеме происходит магия SlowStartInitialBatchSize. То есть, при каждом успешном создании пода, новых подов поднимается в 2 раза больше. Это сделано, чтобы не упороть KubeApiserver, если что-то пойдет не так.
      
  - `Informers`:  
    - Информер - сущность, позволяеющая контроллерам подписываться на события хранилища и легко составлять список интересующих их ресурсов.  
    - Умеет, например, кешировать.  
  - `Scheduler`:  
    - Слушает события, шедулит поды на ноды в соответствии с запрошенными ресурсами/параметрами.  
  - `Kubelet`:  
    - Это агент, запущенный на каждой воркер ноде кластера k8s и отвечает, например, за управление жизненным циклом подов. Он обрабатывает всю логику перевода между абстракцией "Pod" и ее строительными блоками, контейнерами.  
    - Он также обрабатывает всю сопутствующую логику, связанную с:  
      - монтированием томов  
      - протоколированием контейнеров  
      - сборкой мусора и многими другими важными вещами  
      - передачей `podSpec` в `CRI`  
  - `CRI` (Docker, containerd (protocol buffers (it's like a faster JSON) and a gRPC API)):  
    - Cоздается `Sandbox` (песочница) включает в себя создание `pause` контейнера.  
    - `pause` контейнер служит в качестве родительского для всех остальных контейнеров в `Pod`, поскольку в нем размещается множество ресурсов уровня `Pod`, которые в конечном итоге будут использовать контейнеры рабочей нагрузки.  
    Эти `ресурсы` представляют собой пространства имен `Linux` (IPC, сеть, PID).  
  - `CNI`:  
    > bridge/ipvlan/macvlan/sr-iov
    
    тут прокидывается виртуальный линк в `Pod` хоста, `IP` цепляется за `pause` контейнер, чтоб не потеряться при рестартах контейнера из-за ошибок, например.  
  - `Inter-host networking`:  
    - `overlay networking` (Flannel, например)  
    Для этого обычно используется концепция оверлейной сети, которая представляет собой способ динамической синхронизации маршрутов между несколькими узлами. 
    Одним из популярных поставщиков оверлейных сетей является `Flannel`. Когда он установлен, его основной задачей является обеспечение сети `IPv4` третьего уровня между несколькими узлами в кластере. 
    `Flannel` не управляет тем, как контейнеры подключаются к узлу (это задача `CNI remember`), а скорее тем, как трафик передается между узлами. 
    Для этого он выбирает подсеть для узла и регистрирует ее в `etcd`. Затем он хранит локальное представление маршрутов кластера и инкапсулирует исходящие пакеты в UDP-датаграммы, гарантируя, что они дойдут до нужного узла.  
    > Для получения дополнительной информации ознакомьтесь с документацией CoreOS.  
  - `Container startup`: 
    - Pull the image  
    - Create the container via CRI  
    - Create network via CNI (всякие правила iptables)  
    - post-start lifecycle хуки  
    - Рединес пробы  
    - Контейнер шуршит  
  
#### Компоненты контура управления Kubernetes  
  - `Kube-apiserver`:  
    - представляет API Kubernetes;  
    - умеет в горизонтальное масштабирование;  
    - на OpenAPI (OpenAPI - это cпецификация), на архитектуре REST.  
  - `etcd`:  
    - Распределённая и высоконадёжная БД в формате "ключ-значение", основное хранилище всех данных кластера в Kubernetes.  
  - `kube-scheduler`:  
    - отслеживает созданные поды без привязанного узла (ноды) и выбирает узел, на котором они должны работать;  
    - назначает поды согласно требованиям к ресурсам, ограничениям, связанным с аппаратными/программными политиками, принадлежности (affinity) и непринадлежности (anti-affinity) узлов/подов, местонахождению данных, предельным срокам отклика.  
  - `kube-controller-manager` (куча контроллеров в одном бинаре):  
    - `Node Controller`: уведомляет и реагирует на сбои узла;
    - `ReplicationController`: старая, изначальная технология, сейчас этой балалайки в `k8s` нет;
    - `ReplicaSets Controller`: поддерживает правильное количество подов для каждого объекта `ReplicaSets` в системе. У него нет `rolling-update`, как у предшественника. Вот по этому появился `Deployment`, он абстракция над `ReplicaSets`, добавляет функционал `rolling-update/rollback`. Костыли. Кругом костыли;  
    - `Endpoints Controller`: заполняет объект узлов (`Endpoints`), то есть связывает сервисы (`Services`) и поды (`Pods`);  
    - `Account & Token Controllers`: создают стандартные учетные записи и токены доступа API для новых пространств имен.  
> Контроллер - это асинхронный скрипт, который работает над согласованием текущего состояния системы `Kubernetes` с желаемым состоянием. Полезно думать о кубелете как о контроллере! Он запрашивает `Pods` из `kube-apiserver` каждые 20 секунд (это настраивается), фильтруя те, чье `NodeName` совпадает с именем узла, на котором запущен `kubelet`. Получив этот список, он обнаруживает новые добавления, сравнивая их с собственным внутренним кэшем, и начинает синхронизировать состояние, если имеются какие-либо расхождения.  
   
#### Компоненты worker-ноды Kubernetes  
  - `kubelet`:  
    - следит за тем, чтобы контейнеры были запущены в поде;  
    - принимает набор `PodSpecs`, и гарантирует работоспособность и исправность определённых в них контейнеров;  
    - если `Pod` создается, он регистрирует некоторые метрики запуска, в `Prometheus` для отслеживания `Pod`;  
   
> У пода бывает несколько статусов: `Pending, Running, Succeeded, Failed and Unknown`. Когда `Pod` запускается впервые, `Kubelet` вызывает команду удаленной процедуры `RunPodSandbox (RPC)`. Песочница" - это термин `CRI` для описания набора контейнеров, который в языке `Kubernetes`, как вы догадались, является `Pod`.  

  - `kube-proxy`:  
    - конфигурирует правила сети на узлах (iptables). При помощи них разрешаются сетевые подключения к вашим подам изнутри и снаружи кластера;  
> kube-proxy использует уровень фильтрации пакетов в операционной системы, если он доступен. В противном случае, kube-proxy сам обрабатывает передачу сетевого трафика.  

#### Общие вопросы по Kubernetes  
  - Как выбирается мастер в k8s: RAFT  
  - По какому протоколу API общается: OpenAPI (REST) HTTP/HTTPS  
  - Пробы:  
    - `livenessProbe`: Показывает, запущен ли контейнер;  
    - `readinessProbe`: Указывает, готов ли контейнер отвечать на запросы;  
    - `startupProbe`: Указывает, запущено ли приложение внутри контейнера.  
    > Нужно выбирать или `livenessProbe` + `readinessProbe`, или `startupProbe`. Если с пробами что-то не так, `kubelet` смотрит в `restartPolicy`, а они бывают трех видов - `Always, OnFailure, and Never`
  - Как прокидывается файл из инит контейнера: согласно описаным в `volumeMounts` правилам

  - Восстановление etcd (disaster recovery):
    - нужно выключить 2 из трех инстансов, на оставшемся можно подложить последний хороший бэкап (забэкапив текущие данные, если они покрашились) и запуститься с ключем `--force-new-cluster`
    - [ETCD Disaster recovery](https://etcd.io/docs/v3.3/op-guide/recovery/)  
    > Сжатие + дефрагментация + правильный мониторинг — основа обслуживания вашего кластера etcd.

  - Два слова про `REST`. Обычно существует 2 поля объекта: `spec` и `status`.  
    В поле `spec` указывается требуемое состояние (описание характеристик, которые должны быть у объекта).
    `status` описывает текущее состояние объекта
    ой как понятно стало  
  - `garbage collector` вычищает по полю `ownerReferences`  

#### Сущности Kubernetes   
  - `StatefulSets`: Штука, описывающая где будут крутиться `Pods` с данными. [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) 
  - `Daemonset`: Гарантирует, что все (или некоторые по .spec.template.spec.{nodeSelector или affinity}) узлы запускают копию `Pod`  
  - `Operator`: (профессия) — группа профессий по управлению работой оборудования (установок) различного вида и назначения. Шутка. `Операторы` - это программные расширения `Kubernetes`, которые используют пользовательские ресурсы для управления приложениями и их компонентами.  
  К числу задач, которые можно автоматизировать с помощью оператора, относятся:
    - развертывание приложения по требованию;  
    - создание и восстановление резервных копий состояния приложения;  
    - обработка обновлений кода приложения вместе с сопутствующими изменениями, такими как схемы баз данных или дополнительные параметры конфигурации;  
    - публикация службы для приложений, которые не поддерживают API Kubernetes, чтобы обнаружить их;  
    - имитация сбоя всего кластера или его части для проверки его устойчивости; 
    - выбор лидера для распределенного приложения без внутреннего участника.  

#### Сеть в Kubernetes
  - `Service`:
    Для некоторых частей вашего приложения (например, фронтендов) вы можете захотеть на `Service` повесить внешний IP-адрес, доступный за пределами вашего кластера.  
    - [Service Type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) в `Kubernetes` позволяет указать, какой тип сервиса вам нужен.
      Доступны следующие значения типов и их поведение:
      - `ClusterIP`: предоставляет службе (`Service`) внутренний IP-адрес кластера. При выборе этого значения служба будет доступна только из кластера. Это значение используется по умолчанию, если вы явно не указали `Service Type`. Вы можете открыть службу для публики с помощью `Ingress` (обычный путь) или `Gateway API`.
      - `NodePort`: предоставляет службу на IP-адресе каждого узла через статический порт (NodePort). Чтобы сделать порт узла доступным, Kubernetes устанавливает кластерный IP-адрес, так же как если бы вы запросили `Service Type`: `ClusterIP`.  
      - `LoadBalancer`: Предоставляет службу извне, используя балансировщик нагрузки облачного провайдера.  
      - `ExternalName` (Внешнее имя): Сопоставляет службу с содержимым поля externalName (например, foo.bar.example.com), возвращая запись CNAME с его значением. Никакого проксирования не устанавливается.  

  - `Pause контейнер` держит `netns`  
    - У каждого пода свой уникальный IP  
    - На каждой ноде есть root netns. Основной сетевой интерфейс — eth0 — находится в этом root netns  
    - У каждого пода есть свой netns с виртуальным интерфейсом Ethernet, связывающим их с root netns (ip link)  
    - Это виртуальный линк с одним концом в root netns и другим — в netns пода  
  
  - Предположим, пакет отправляется из pod1 в pod2 внутри одной ноды:  
    1. Он через eth0 покидает netns, принадлежащий pod1, и попадает в root netns через vethxxx.  
    2. Попадает в cbr0, который выдаёт ему точку назначения с помощью ARP-запроса, спрашивающего «У кого такой IP-адрес?».  
    3. vethyyy отвечает, что у него нужный IP — так мост узнаёт, куда переслать пакет.  
    4. Пакет достигает vethyyy и, проходя виртуальный линк, попадает в netns, принадлежащий pod2.  
    *поды, также, должны быть доступны из всех узлов (со всех нод).  
    
  - Взаимодействие между узлами (inter-node):
    Поды также должны быть доступны из всех узлов. И для Kubernetes вовсе не принципиально, как это реализовано. Можно использовать L2 (ARP между узлами), L3 (IP-маршрутизация между узлами — аналогично таблицам роутинга у облачных провайдеров), оверлейные сети и даже почтовых голубей.  
    
    Каждому узлу назначается уникальный блок `CIDR` (диапазон IP-адресов) для IP-адресов, выдаваемых подам, так что у каждого пода свой уникальный IP, не конфликтующий с подами других узлов.  

## Команды дебага Linux  
```bash
  lsof -p # поиск удаленных файлов, если процесс их еще держит
  numactl --hardware, -H # список номеров нод, разделенных запятыми, или диапазонов A-B, или всех.

  perf: # узнать сколько CPU использует каждая функция в программе
    CPU:
      perf top
      perf stat ls -e
      perf 
  /usr/bin/perf top -c 100

  strace # отслеживает системные вызовы
    strace -e trace=%network -p <PID> # смотреть сетeвые вызовы
    strace -f -p <PID> # посмотреть все дочерние процессы
    strace -e open -p <PID> # посмотреть все файлы, которые открывает процесс

  unshare # запуск программ в пространстве имен, не разделенном с родительским.
  ulimit -n # фиксит Too many open files
  opensnoop # следит за открытыми файлами
  dstat # сочетает в себе возможности iostat, vmstat, netstat и ifstat.
Докер:
  docker ps 

Ресурсы по ядру:
  syscalls https://man7.org/linux/man-pages/man2/syscalls.2.html
    The system call is the fundamental interface between an application and the Linux kernel.
Сетевые: 
  nslookup # DNS запросы
  tcpdump # можно проверить проходит ли пакет между хостами. Через wireshark можно посмотреть кто виноват, клиент или сервер. 
  tcpdump -A # посмотреть пакеты, если трафик не шифрованный
  tcpdump -ni any net 10.232.232.0/31 -AvX 
    -A # Печать каждого пакета (за вычетом заголовка уровня соединения) в формате ASCII. Удобно для захвата веб-страниц.
    -v # verbose
    -X # Печать данных каждого пакета в шестнадцатеричном формате и ASCII. 
  sudo ngrep -d any # сканить сетку
```

Чаще всего, программа работает медленно из-за:  
  - CPU time;  
  - Диска (много I/O оперпаций);  
  - Ожидания медленного сервера.  

Mastering the mentioned tools: (strace, tcpdump, netstat, lsof, ngrep, etc)  

**Ip ip over tcp или нет?**: Нет. TCP - L4, а IPIP и GRE-туннели — это туннели сетевого уровня (L3) модели OSI.
  IPIP и GRE-туннели — это туннели сетевого уровня (L3) модели OSI, при создании которых доступны IP-адреса обеих сторон. Они представляются в системе в виде интерфейсов GreX и IPIPX, и через них можно настраивать маршрутизацию (в том числе и default route) точно также, как и через любые другие интерфейсы.  
  Плюс ко всему для этих интерфейсов можно настроить уровень доступа security level — private, protected или public  
  IPIP (IP over IP) один из самых простых в настройке туннелей (инкапсулирует только unicast IPv4-трафик). Его можно настроить как на UNIX/Linux-системе, так и на различных маршрутизаторах (например, Cisco).  

**Как ООМ выбирает кого убивать?**: По приоритету. Приоритет в файле `/proc/$PID/oom_adj`. Сначала сдохнут свежие процессы пользователя с низким приоритетом, в последнюю очередь рутовые. Диапазон от -1000 (OOM Killer пройдет мимо) до 1000 (Процесс будет дохнуть в числе первых). ~~fsnotify~~

`UEFI`: новый `BIOS`  
`Stage boot loader`: синий экран загрузки, где можно задать `Single mod`. Представьте себе, и за знание таких терминов спрашивают. Еще бы спрашивали какой драйвер за вывод курсора на винде отвечает...   
`SIGHUP`: Сигнал HUP (повесить трубку) примерно такой же, как `SIGTERM` с точки зрения резкости, но у него есть особая роль, поскольку он автоматически отправляется приложениям, работающим в терминале, когда пользователь отключается от этого терминала. Это сигнал номер 1.  
**The signals SIGKILL and SIGSTOP cannot be caught or ignored**  

#### Методы мониторинга  
  - `RED Method`:  
    - Requests  
    - Errors  
    - Duration  
  - `4 golden signals`:  
    - Задержка (Latency)  
    - Трафик (Traffic)  
    - Ошибки (Errors)  
    - Насыщенность (Saturation)  

## Общие вопросы с собесов  
#### Процессы и треды (шаринг ресурсов)
  Поток — определенный способ выполнения процесса. Когда один поток изменяет ресурс процесса, это изменение сразу же становится видно другим потокам этого процесса.
  IP пода делится между всеми его контейнерами и является доступным (маршрутизируемым) для всех остальных подов. 
  Отказоустойчивый, распределенный сервис DNS, например, на 5 зон  

`DNS tcp или udp`: Как правило, считается, что DNS использует UDP port 53, но TCP port 53 также зарезервирован под использование для DNS. 
То есть, (маленький тупой) рекурсивный сервер должен сначала пробовать выполнять DNS-запрос с использованием UDP, но при высокой вероятности большого и усеченного ответа, либо при наличии открытой TCP-сессии к запрашиваемому серверу (по которому обрабатывается другой запрос или запрос другого клиента), не возбраняется использование TCP.
Подробнее [тут](https://www.securitylab.ru/blog/personal/aodugin/296669.php)  

`Теорема cap`: эвристическое утверждение о том, что в любой реализации распределённых вычислений возможно обеспечить не более двух из трёх следующих свойств:  
  - согласованность данных (англ. consistency) — во всех вычислительных узлах в один момент времени данные не противоречат друг другу;  
  - доступность (англ. availability) — любой запрос к распределённой системе завершается откликом, однако без гарантии, что ответы всех узлов системы совпадают;  
  - устойчивость к разделению (англ. partition tolerance) — расщепление распределённой системы на несколько изолированных секций не приводит к некорректности отклика от каждой из секций.  

#### Вопросы от Барсукова  
  У вас есть ноутбук с линуксом, например убунтой, на рабочем столе запущен терминал,
  в нем вы запускаете curl https://example.com/расскажите, что произойдет?

  Прострой отказоустойчивый сервис сокращения ссылок, например.  

#### Шифрование 
  - Симметричное шифрование - один и тот же ключ используется и для кодирования, и для восстановления информации:  
    - Шифр Цезаря, RSA  
  - Асимметричное шифрование - данные шифруются открытым ключем, а расшифровываются приватным. И никакой магии. Примеры:    
    - TLS, SSH.   
    - mTLS добавляет возможность двусторонней аутентификации. Это означает, что не только клиент, но и сервер должны предоставить свидетельство своей подлинности при установлении защищенного соединения. Такое усиление аутентификации снижает риск атаки «человек посередине», когда злоумышленник пытается подставиться под сервер или клиента.  
      
#### Типы баз данных  
  - Реляционные - SQL (мощная аналитика):   
    - PostgreSQL  
    - MySQL  
    - MariaDB  
    - Oracle  
    - SQLite  
  - NoSQL - документные, похожие на Json (Быстрый доступ к конкретной информации):  
    - MongoDB  
    - CouchDB  
  - NoSQL - key: value (Ключ: значение)  
    - Redis  
    - Memcached
    - ETCD  
  - NoSQL - Временные ряды:  
    - Prometheus  
    - TimescaleDB  
  - NewSQL:  
    - ...  
  - Графовые:  
    -  Dgraph
    -  Giraph
#### Свистелки
  `Argo cd` (continuous delivery): декларативный инструмент для непрерывной доставки в Kubernetes по модели `GitOps`  
  `Terraform (IaC)`: управляет внешними ресурсами поставщиков услуг, например, облачная инфраструктура, инфраструктура частного облака, сетевые устройства, программное обеспечение как услуга и платформа как услуга;  
  `Istio Service Mesh`:
    - `Istio` идет как `Control Plane`, он состоит из трёх компонентов - `Pilot`, `Mixer` и `Citadel`;  
    - `Envoy` как `sidecar` у подов (Data Plane)  
      > Istio перехватывает весь сетевой трафик и применяет к нему набор правил, вставляя в каждый pod умный прокси в виде sidecar-контейнера. Прокси, которые активируют все возможности, образуют собой Data Plane, и они могут динамически настраиваться с помощью Control Plane.  
    > На моей практике `Nginx` сайта перенаправлял запросы к одной из нескольких ферм `Envoy`, которая роутила запрос непосредственно в нужный `kubernetes` кластер. 
    
  `ELK: (Elasticsearch, Logstash и Kibana)`: у нас ClickHouse, c kittenhouse - своей проксей + statsd  
  `sr-iov`: Single Root Input/Output Virtualization  
  `Calico`: сетевая штука, через `CRD` (Custom Resource Definition) поднимает `networkpolicy`, `net`  
  `Consul`: обеспечивает обнаружение сервисов, проверку работоспособности, балансировку нагрузки, граф сервисов, принудительное использование идентификационных данных с помощью TLS и управление конфигурацией распределенных сервисов. Вау.    
  `Mesos`: это централизованная отказоустойчивая система управления кластером. Она разработана для распределенных компьютерных сред c целью обеспечения изоляции ресурсов и удобного управления кластерами подчиненных узлов (mesos slaves). Это новый эффективный способ управления серверной инфраструктурой, но и, как любое техническое решение, не "серебряная пуля". Нормальные мальчики пользуют ванильный кубер :)  
  `Apache Kafka`:  
    - Событие или сообщение — данные, которые поступают из одного сервиса, хранятся на узлах Kafka и читаются другими сервисами. Сообщение состоит из:  
      - Key — опциональный ключ, нужен для распределения сообщений по кластеру.  
      - Value — массив байт, бизнес-данные.  
      - Timestamp — текущее системное время, устанавливается отправителем или кластером во время обработки.  
      - Headers — пользовательские атрибуты key-value, которые прикрепляют к сообщению.  

## Менеджерские свистелки
  `Nexus`: фреймворк - расширение классического скрама для крупных проектов с многокомандной разработкой.  
  `ITIL методология` (главное - не опечататься): https://www.atlassian.com/ru/itsm/itil
  `ITSM методология` Основная идея ITSM заключается в том, что ИТ нужно предоставлять как услугу.

## Вопросы без ответа 
  Понимание BGP: это протокол динамической маршрутизации  

  Ansible: range или to yaml (второе не мержит)  
  Dependencies  
  lvm  
  jagger
  openapi 
  gravitee  
  vm ware - виртуализация, не интересно в эпоху контейнеров. Хотя... Есть люди, которые поднимают `Kubernetes` в виртуалках, наверно, надо изучить эти кейсы. Здесь может быть ваш MR :)  
  LeetCode - уровень easy https://leetcode.com/ - это для SRE в Rндекс и ТинькоFF. Кстати, они гоняют тупо по академическим знаниям, не спрашивая у любителей куберетиса ничего про кубернетис, отнимая тонны вашего времени на 4 этапа. Что сказать, Google Way...  

dochouse
штурвал 
haiva
ipv6

git джит-компилятор

Terraform + Yandex Cloud
Пишут модули
Terragrand 

copy on write 

steal
dora 
dhcp 
acid 

catacontainer
Безопасность:
  dlp системы

  TRIBE
  RHEL
  Пайпы
