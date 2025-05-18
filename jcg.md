
# 정보처리기사 2024년 1회차 오답 노트 (상세 해설)

아래는 1회차 기출에서 틀린 문항들에 대한 상세 해설입니다. 각 문항별 핵심 개념과 이유를 꼼꼼히 확인하세요.

---

## 1번. Coad-Yourdon 분석 방법론 (정답: ①)
- **정답 선택지**: ① 마이크로/매크로 프로세스를 모두 사용한다
- **해설**: Coad-Yourdon 기법은 객체 지향 분석 기법으로, 시스템을 분석할 때 **마이크로 프로세스(상세 기능)**와 **매크로 프로세스(전반적 흐름)**를 모두 사용하여 객체와 클래스 모델을 도출합니다. 이 과정을 통해 클래스의 책임, 메시지 흐름 및 객체 간 인터페이스를 명확히 정의합니다. citeturn0file0

---

## 3번. DFD 4대 요소 (정답: ②)
- **정답 선택지**: ② 단말(Terminator)
- **해설**: DFD(Data Flow Diagram)의 구성 요소는 다음 네 가지입니다:
  1. **프로세스(Process)** – 데이터 처리 활동
  2. **데이터 흐름(Data Flow)** – 데이터 전송 경로
  3. **데이터 저장소(Data Store)** – 데이터 보관 장소
  4. **단말(Terminator)** – 시스템 외부 엔터티 또는 인터페이스 citeturn0file0

---

## 7번. Rumbaugh 객체 모델링 단계 (정답: ①)
- **정답 선택지**: ① 객체 추출 → 속성·연산 정의 → 관계 규정 → 계층 구조화
- **해설**: Rumbaugh 방법론(Object Modeling Technique)은 다음 순서로 진행됩니다:
  1. **객체 식별(Object Identification)**
  2. **속성·연산 정의(Attribute & Operation Definition)**
  3. **관계 규정(Relationship Definition)**
  4. **클래스 계층 구조화(Class Hierarchy Formation)**
  두 번째 단계인 속성 및 연산 정의가 핵심입니다. citeturn0file0

---

## 8번. State vs Sequence Diagram (정답: ④)
- **정답 선택지**: ④ 상태 변화 vs 메시지 교환
- **해설**:
  - **State Diagram**: 객체가 가질 수 있는 상태(State)와 상태 전이(Transition) 모델링
  - **Sequence Diagram**: 객체 간 메시지(Message) 흐름 및 호출 순서 모델링
  각각의 목적이 다름을 구분해야 합니다. citeturn0file0

---

## 10번. Bridge 패턴 (정답: ③)
- **정답 선택지**: ③ 추상부와 구현부 분리
- **해설**: Bridge 패턴은 **Abstraction**(추상부)와 **Implementor**(구현부)를 분리하여, 두 부분을 독립적으로 확장할 수 있도록 설계하는 구조 패턴입니다. 이를 통해 구현 세부사항에 영향을 받지 않고 추상화를 변경할 수 있습니다. citeturn0file0

---

## 11번. XP의 핵심 (정답: ①)
- **정답 선택지**: ① 자동화된 지속적 테스트
- **해설**: eXtreme Programming(XP)은 **지속적 통합(Continuous Integration)**과 **지속적 테스트(Continuous Testing)**를 자동화하여, 빠른 피드백과 짧은 릴리즈 주기를 유지하는 애자일 개발 방법론입니다. citeturn0file0

---

## 15번. 비기능적 요구사항 (정답: ②)
- **정답 선택지**: ② 처리 성능·반응시간·보안·안전
- **해설**: 비기능적 요구사항(Non-functional Requirements)은 시스템이 **어떻게** 동작해야 하는지를 정의하며, 대표적으로 성능(Performance), 반응시간(Response Time), 신뢰성(Reliability), 보안(Security), 안전(Safety) 등을 포함합니다. citeturn0file0

---

## 17번. SOLID 원칙 (정답: ④)
- **정답 선택지**: ④ SSO는 잘못된 조합
- **해설**: SOLID는 다음 다섯 가지 설계 원칙의 약자입니다:
  - S: Single Responsibility Principle
  - O: Open/Closed Principle
  - L: Liskov Substitution Principle
  - I: Interface Segregation Principle
  - D: Dependency Inversion Principle
  ‘SSO’는 SOLID 원칙에 속하지 않습니다. citeturn0file0

---

## 19번. CASE 원천 기술 (정답: ④)
- **정답 선택지**: ④ 구조적 기법·프로토타이핑·분산처리·정보 저장소
- **해설**: 전통적 CASE(Computer-Aided Software Engineering) 도구의 기반 기술로는 ‘구조적 기법, 프로토타이핑, 분산 처리, 정보 저장소’ 등이 있습니다. citeturn0file0

---

## 20번. 상태 다이어그램 전이 유발 요인 (정답: ①)
- **정답 선택지**: ① Event
- **해설**: 상태 다이어그램에서 상태 전이는 **Event(이벤트)**가 발생할 때 트리거되며, Guard 조건 및 수행 Action은 전이 내의 부가 요소입니다. citeturn0file0

---

## 22번. Alpha Test (정답: ③)
- **정답 선택지**: ③ 개발자 장소에서 사용자와 함께 수행
- **해설**: Alpha Test는 **개발사 내부** 환경에서 실제 사용자 또는 테스터와 함께 수행하는 초기 검증 단계로, 기능 완성도를 사내에서 확인합니다. Beta Test는 외부 사용자 환경에서 이루어집니다. citeturn0file0

---

## 23번. 트리의 차수(Degree) (정답: ②)
- **정답 선택지**: ② 가장 많은 자식 수
- **해설**: 트리에서 차수(Degree)는 “가장 많은 자식을 가진 노드의 자식 개수”를 의미합니다. citeturn0file0

---

## 25번. 해싱: Folding 기법 (정답: ②)
- **정답 선택지**: ② 키 분할 후 합산
- **해설**: Folding 해싱은 키를 일정 길이 부분으로 **분할**한 뒤, 각 부분을 더하거나 XOR 연산하여 해시 주소를 계산하는 기법입니다. citeturn0file0

---

## 28번. 이진트리 순회: Inorder (정답: ④)
- **정답 선택지**: ④ Left → Root → Right
- **해설**: 중위 순회(Inorder)는 왼쪽 서브트리 방문 → 루트 노드 방문 → 오른쪽 서브트리 방문 순으로 진행됩니다. citeturn0file0

---

## 29번. Base Path Testing (정답: ④)
- **정답 선택지**: ④ 비순환 독립 경로
- **해설**: Base Path Testing은 Cyclomatic Complexity 기반으로 **비순환 독립 경로(Independent Path)**를 도출하여 테스트 케이스를 설계하는 화이트박스 테스트 기법입니다. citeturn0file0

---

## 37번. Total Oracle (정답: ②)
- **정답 선택지**: ② 모든 입력에 대한 기대 결과
- **해설**: Total Oracle은 테스트 입력 값마다 정확한 **기대 결과(Expected Result)**를 제공하는 오라클로, Partial Oracle 대비 완전 검사 성격을 가집니다. citeturn0file0

---

## 38번. 테스트 도구 vs 프레임워크 (정답: ①)
- **정답 선택지**: ① xUnit은 테스트 프레임워크
- **해설**: ESB, STAF, NTAF 등은 구현 검증을 위한 드라이버/스텁 도구(Verification Tools)이며, xUnit(JUnit/NUnit)은 테스트 코드 작성 및 실행을 체계화하는 **테스트 프레임워크**입니다. citeturn0file0

---

## 40번. 파티션 시험기법 (정답: ④)
- **정답 선택지**: ④ Unit Partitioning 없음
- **해설**: 대표적 파티션 시험기법으로는 리스트(List), 범위(Range), 해시(Hash), 카르테시안 조합(Combination) 파티셔닝이 있으며, Unit Partitioning은 존재하지 않습니다. citeturn0file0

---

## 45번. Entity Integrity (정답: ①)
- **정답 선택지**: ① 기본키 널 불가, 원자 값
- **해설**: Entity Integrity(개체 무결성)는 **기본키 컬럼이 NULL이 아니고 단일 원자 값(Atomic Value)**을 가져야 한다는 제약입니다. citeturn0file0

---

## 46번. BCNF 정규형 (정답: ④)
- **정답 선택지**: ④ 후보키 아닌 결정자 제거
- **해설**: BCNF(보이스-코드 정규형)는 모든 결정자(Determiner)가 후보키(Candidate Key) 이어야 하며, 그렇지 않은 함수 종속성을 제거하여 릴레이션을 분해합니다. citeturn0file0

---

## 48번. SQL UPDATE 문 (정답: ②)
- **정답 선택지**: ② UPDATE…SET…WHERE
- **해설**:
```sql
UPDATE 테이블명
   SET 컬럼1 = 값1, 컬럼2 = 값2
 WHERE 조건;
````

WHERE 절 없이 수행하면 전체 행이 수정되므로 주의해야 합니다. citeturn0file0

---

## 49번. 개념 스키마 (정답: ①)

* **정답 선택지**: ① 전체 DB 구조·제약·권한 정의
* **해설**: 개념 스키마(Conceptual Schema)는 DB 전체 구조, 주요 엔터티 및 관계, 제약조건, 사용자 접근권한 등을 정의하는 중간 단계 스키마입니다. citeturn0file0

---

## 51번. 카디널리티 vs 차수 (정답: ②)

* **정답 선택지**: ② Cardinality=행 수, Degree=컬럼 수
* **해설**: Cardinality는 테이블의 **튜플 수(Row Count)**, Degree는 \*\*속성 수(Column Count)\*\*를 의미합니다. citeturn0file0

---

## 52번. 병행제어 vs CPU 스케줄링 (정답: ②)

* **정답 선택지**: ② 시분할(Time-Slice) 아님
* **해설**: 로킹(Locking), 타임스탬프, 다중 버전(MVCC)은 DB **병행 제어(Concurrency Control)** 기법이며, Time-Slice는 CPU **스케줄링** 개념입니다. citeturn0file0

---

## 53번. 이상(Anomaly) 유형 (정답: ①)

* **정답 선택지**: ① 삽입·삭제·갱신
* **해설**: DB 이상(Anomaly)은 삽입 이상, 삭제 이상, 갱신 이상 세 가지이며, 검색 이상(Search Anomaly)은 분류되지 않습니다. citeturn0file0

---

## 54번. 트랜잭션 Isolation (정답: ③)

* **정답 선택지**: ③ 병행 실행 중 간섭 방지
* **해설**: Isolation(격리성)은 트랜잭션이 병행 실행될 때 서로의 작업 결과가 불완전하게 볼 수 없도록 보장하여 **교차 간섭**을 방지합니다. citeturn0file0

---

## 56번. 논리/물리 설계 구분 (정답: ④)

* **정답 선택지**: ④ 인터페이스·데이터 타입·관계 표현
* **해설**: 논리 설계(Logical Design)는 시스템의 데이터 모델을 엔터티, 속성, 관계 중심으로 정의하며, 물리 설계(Physical Design)는 저장소 구조, 인덱스, 파일 조직 등을 다룹니다. citeturn0file0

---

## 60번. DB 유형 구분 기준 (정답: ②)

* **정답 선택지**: ② Relationship
* **해설**: DBMS 유형은 주로 데이터 간 \*\*관계(Relationship)\*\*에 따라 계층형, 네트워크형, 관계형으로 구분합니다. citeturn0file0

---

## 66번. HRN 스케줄링 (정답: ③)

* **정답 선택지**: ③ (대기시간+서비스시간)/서비스시간
* **해설**: Highest Response Ratio Next는 응답비율(대기시간+서비스시간)/서비스시간 순으로 우선순위를 정해 스케줄링 합니다. citeturn0file0

---

## 67번. Java while(y--) (정답: ④)

* **정답 선택지**: ④ x=7, y=-1
* **해설**: y가 0일 때 루프 조건을 확인 후 y를 -1로 감소시키므로, 루프 종료 후 최종 x=7, y=-1이 됩니다. citeturn0file0

---

## 69번. 후위/전위 연산자 (정답: ①)

* **정답 선택지**: ① x=5, y=5, z=5
* **해설**:

```java
// 초기 x=5
y = x++; // y=5, x=6
z = --x; // x=5, z=5
```  

최종 x=5, y=5, z=5입니다. citeturn0file0

---

## 70번. IP 클래스 대역 (정답: ①)
- **정답 선택지**: ① Class A: 1.0.0.0–127.255.255.255
- **해설**: IP 클래스별 대역:
  - Class A: 1.0.0.0 ~ 127.255.255.255
  - Class B: 128.0.0.0 ~ 191.255.255.255
  - Class C: 192.0.0.0 ~ 223.255.255.255 citeturn0file0

---

## 72번. FIFO 페이지 교체 (정답: ②)
- **정답 선택지**: ② 페이지 폴트 14회
- **해설**: 참조 문자열을 FIFO 알고리즘으로 시뮬레이션하면, 초기 프레임 상태와 교체 순서에 따라 총 14회의 페이지 폴트가 발생합니다. 시뮬레이션 표를 참고하세요. citeturn0file0

---

## 76번. IPv6 주소 유형 (정답: ③)
- **정답 선택지**: ③ Broadcast 없음
- **해설**: IPv6는 브로드캐스트 주소 개념을 제거하고, Unicast, Anycast, Multicast만 지원합니다. citeturn0file0

---

## 77번. Control Coupling (정답: ③)
- **정답 선택지**: ③ 하위→상위 모듈 제어
- **해설**: Control Coupling은 한 모듈이 다른 모듈에 **제어 정보(Control Flag)**를 전달하여 실행 흐름을 제어하는 결합도입니다. citeturn0file0

---

## 78번. ARP 프로토콜 (정답: ②)
- **정답 선택지**: ② IP→MAC 변환
- **해설**: ARP는 네트워크 계층 IP 주소를 링크 계층 MAC 주소로 매핑하는 프로토콜로, 로컬 네트워크 내에서 동작합니다. citeturn0file0

---

## 79번. Working Set (정답: ④)
- **정답 선택지**: ④ 자주 참조 페이지 집합
- **해설**: Working Set 이론은 프로세스가 일정 기간 동안 참조한 페이지의 집합을 유지함으로써 페이지 폴트를 최소화하는 메모리 관리 기법입니다. citeturn0file0

---

## 80번. CSMA/CA (정답: ③)
- **정답 선택지**: ③ Collision Avoidance
- **해설**: CSMA/CA(Carrier Sense Multiple Access with Collision Avoidance)는 무선 LAN에서 충돌을 미리 예방하기 위해 RTS/CTS 메커니즘을 사용하여 전송 권한을 조정합니다. citeturn0file0

---

## 81번. IDS Misuse vs Anomaly (정답: ①)
- **정답 선택지**: ① Signature 기반
- **해설**: Misuse Detection(시그니처 기반)은 알려진 공격 패턴(Signature)을 탐지하며, Anomaly Detection은 비정상 행동 패턴을 학습하여 탐지합니다. citeturn0file0

---

## 82번. HACMP (정답: ①)
- **정답 선택지**: ① IBM AIX 클러스터 고가용성
- **해설**: HACMP(High Availability Cluster Multi-Processing)는 IBM AIX 환경을 위한 **클러스터 기반 고가용성(HA) 솔루션**입니다. citeturn0file0

---

## 83번. NFC 약어 (정답: ②)
- **정답 선택지**: ② Near Field Communication
- **해설**: NFC는 "Near Field Communication"의 약어로, 약 10cm 이내 근거리 무선 통신 방식을 뜻합니다. citeturn0file0

---

## 84번. 세션 하이재킹 탐지 (정답: ①)
- **정답 선택지**: ① FTP SYN만으로 불충분
- **해설**: 세션 하이재킹 탐지 기법은 단일 패킷 모니터링이 아닌, **세션 무결성 검사**(예: SSL/TLS, 세션 토큰 검증)와 연계해야 합니다. citeturn0file0

---

# 암기용 요약 노트

시험 직전 빠르게 훑어볼 **핵심 키워드** 모음입니다.

| 문항  | 키워드                                  | 문항 | 키워드                        |
|:-----:|:---------------------------------------|:----:|:------------------------------|
| 1     | Coad-Yourdon: 마이크로/매크로          | 56   | 논리설계: 엔터티·관계        |
| 3     | DFD 4요素: 프로세스·흐름·저장소·단말   | 60   | DB 유형: Relationship        |
| 7     | Rumbaugh: 속성·연산 정의               | 66   | HRN = (대기+서비스)/서비스   |
| 8     | State vs Sequence                      | 67   | while(y--): x=7, y=-1       |
| 10    | Bridge: 추상부·구현부 분리            | 69   | y=x++;z=--x → 5,5,5         |
| 11    | XP: 지속적 테스트 자동화              | 70   | Class A: 1.0.0.0–127.255...  |
| 15    | 비기능 요구: 성능·보안·안전            | 72   | FIFO 폴트=14회                |
| 17    | SOLID (SRP,OCP,LSP,ISP,DIP)            | 76   | IPv6: Broadcast 없음         |
| 19    | CASE: 구조·프로토타입·분산·저장소      | 77   | Control Coupling            |
| 20    | 전이 유발: Event                       | 78   | ARP: IP→MAC                 |
| 22    | Alpha Test 내부+사용자                | 79   | Working Set                  |
| 23    | 트리 차수: 최대 자식 수                | 80   | CSMA/CA                      |
| 25    | Folding 해싱: 분할+합산                | 81   | IDS: Signature vs Anomaly   |
| 28    | Inorder: L→Root→R                      | 82   | HACMP: AIX HA                |
| 29    | Base Path: 독립경로                    | 83   | NFC: 근거리 무선            |
| 37    | Total Oracle: 전 입력 기대 결과       | 84   | 세션 무결성 필요             |
| 38    | xUnit = 프레임워크                     | 88   | COCOMO: Sequential 없음      |
| 40    | Unit Partitioning 없음                | 89   | MAC: 중앙 관리자 고정       |
| 45    | Entity Integrity: PK 널 불가, 원자값   | 91   | CBD 산출: 요구사항 정의서   |
| 46    | BCNF: 후보키 아닌 결정자 제거          | 93   | Resource Injection 없음     |
| 48    | UPDATE…SET…WHERE                     | 96   | Porting: OS/하드웨어 이식     |
| 49    | 개념 스키마: 구조·제약·권한           | 99   | SPICE: 프로세스 개선 모델    |
| 51    | Cardinality=행, Degree=열              | 100  | SPICE: 프로세스 개선 모델    |
