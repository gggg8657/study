![alt text](image.png)
Semantic Kernel = Lang Chain
---
- demo 
    - req(text) -> azure ai -> response( Romantic, Sentimental, ... Semantic Keyword)  -> spotify (spotify playlist)
    - ! 요즘 노래, 내가 아는 노래 하나도 안나옴
        - 뭔가 어설퍼
    - melon top 100 을 리스트업을 해서, 플리를 만들자? 
        - 차트 다운 받아야겠네 -> no API
        - 크롤링 해야되네
        - 야스셰이빙 시작 <-
            - 공부 TODO : 셀레늄, 퍼피티어, 
        - spotify에 멜론차트 이미 있노 
        - 키워드 받아서, 플리 만드는 API 가 있고, 
            - <b>insight 😀:</b> Valence 가 spotify 에도 있네
        - 감정을 수치로 바꿔보자 <- :: Valence, Danceability 는 수치로 나온다.

- Semantic Kernel
    - 
    1. What 
        - Lang chain <- python 만 지원
        - recent AI model orchestration Tool
        - .NET/ Pytho/ Java 모두 지원
        - MS Copilot 이 이걸로 만들어짐
    2. Support
        - OpenAI/ Azure/ Ollama/ Hugging Face/ Mistral AI/ Google Gemini
    3. sellect
        - 넓은 생태계 Lang Chain
        - 공식적인 지원 Semantic Kernel

    ---
    4. how does it work
        - Polyglot Notebook <- Python ... 
        - ㅈㄴ 쉽게 불러서 갖다 쓸 수 있음 Semantic Kernel 고려해보기
    5. 이거 ㅅㅂ 자동사냥인데
        - 토큰 사용량이 ㅈㄴ 늘어남
        - 음악 플리 만들라고 뭐 하는건데, <- 감정 분석 하고, <- 
        - 확인하는 절차로는 쓸 수 있겠지만, 
        - manual 하게 컨츄롤 하는것도 좋을거 같다.
    <h2> 정리 </h2>

    개사기 자동사냥 툴 있는데,

    지금은 존나 비싸니까, 수동으로 해야되는게 있을꺼야

    그런데, 개사기 자동사냥에서, 자동으로 돌아가는 과정을 출력을 통해서 어떤 모듈들이 불러와지는지 확인하고,
    
    그 모듈들 수기로 연결해주고 자동사냥 꺼라.

    * <b>insight 😀:</b> API 불러오면서 few shot 조져주는거도 ㄱㅊ은듯?
    - <b>insight 😀:</b> prompt 를 짜서, 그거로 랭기쥐 모델에 넣어주는거? 도 방법이지?

    - <b>insight 😀:</b> RAG pattern 은 최신 데이터를 프롬프트에 추가하여 최신 결과를 내보낼 수 있는 가장 쉬운 방법

    - <b>insight 😀:</b> json 형태를 써야지... 그치... 그게 맞지