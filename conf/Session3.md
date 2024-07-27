post Math

![alt text](image-2.png)


GPT 
# Sangjoon Han

## Career Overview
- **Expertise**: CCTV person detection, face recognition, Document AI
- **Experience**:
  - Fast Campus
  - Upstage
  - **Specialization**: OCR

## Skills
- **Backend/Frontend**
- **Mobile Development**
- **Computer Vision (CV)**
- **Deep Learning (DL)**

## Current Challenges
- **OCR Mastery**: Not fully achieved.

## Key Target
- **Code Lab**: Seems highly challenging and comprehensive.

## Post Math Project

### Educational Business Strategy
- **Problem Definition**: How to generate profit, considering costs and other factors.
- **Approach**:
  - Define current state ("As Is")
  - Define desired state ("To Be")
  - Define necessary changes ("Should Be")
  - Implement and evaluate solutions to verify hypotheses.

### Personalized Learning in Math
- **Challenges**:
  - Difficulty in implementation.
  - Similar issues faced by services like Kumon and Noonnoppi.
  - High-quality tutoring is often expensive and not widely accessible.
- **Solution**: Use tools to bridge the gap, although tools also incur costs.

### Math Assistant: Digital Content Creation Platform
- **Data Handling**: Converting unstructured data into structured formats for easier processing.
- **Content Creation**:
  - Upload original test papers.
  - Extract questions, formats, scoring, equations, and additional information for database entry.
  - Handle messy handwritten notes on solved test papers using advanced OCR techniques.
  - Implement question area separation using YOLO-based methods for detailed segmentation.

### Challenges in Data Processing
- **Data Bias**: High variance in data quality can impact model performance.
- **Augmentation**: Use tools like Augraphy for document augmentation and generate synthetic data for OCR training.

### Data Structure
- **Image Processing**:
  - Normalization, text detection, recognition, and restructuring.
  - Use scene text detection models and segment maps for better text extraction.
  - Crop images and perform text recognition with vision encoders and text decoders.

### Unresolved Issues
- **In-Doc OCR**:
  - Latex OCR model integration.
  - Fixing inaccuracies in YOLO detections.
  - Retraining models for specific tasks.

### Advanced Models
- **NAVER DEER**: End-to-end OCR model learning.
- **Document Layout Analysis**:
  - Text and image recognition for structured data extraction.
  - Ensure accurate key-value pairings and groupings.

### Future Directions
- **LLM to LMM**: Transitioning from language models to multimodal models.
- **Math Content Creation**:
  - Despite advances, fully automated solutions remain inadequate for professional-grade explanations.
  - Specialized human-created explanations are still more effective.
  - Multimodal models are necessary for handling image-based content.

### Competition Insights
- **Kaggle Math Olympiad**:
  - Used Latex-formatted problems.
  - Top scores indicate current limitations of AI in solving advanced math problems.

### Key Issues in Math AI
- **Solution Approach**:
  - Using symbolic computation tools like Sympy to solve problems.
  - Implementing agent-based problem-solving frameworks.

---

**Note**: This document provides an overview of Sangjoon Han's career, current projects, challenges, and insights into developing advanced AI solutions for educational content creation, especially in the field of mathematics.

원문:
Sangjoon Han 
CV -> cctv 사람 검출, face recognition ., etc
-> document AI 

Fast campus -> upstage -> <b>OCR </b>

BE/ FE/ Mobile / CV/ DL ...


------------------------------------------------

깊게 들어갈 수 없는 부분들 있다. 
- OCR 정복 안됨. 

Key target is ↑

Code lab 이 진빼이 같네... ㄲㅂ


"Post Math"

수학을 교육 사업으로 풀어낼때, 방향성

문제 정의 -> 이윤 창출 해야되는데 ... 비용적인거 등등 포함

	잘 되게끔 풀어주면 됨 (ㅈㄴ 자명하노)

As Is 

To be 

should be

이 단계는 기본이고

실행을 해봤을때, 평가를 통해서, 우리의 가설이 맞는지 

그래서, 해결책들의 모음이 솔루션이 된다고 본다.

개인별 맞춤 교육-> 수학에서 어케함? ->
디지털 교과서고 자시고...

크게 보면
개인별 맞춤 학습은 교육이니까, 교육자가 있는데, 그걸 교사 혹은 AI 튜터가 되는건데

- 사실 잘 안되는게 맞는데
- 해봤는데, 안합니다.
- 구몬, 눈높이 밀리는거랑 똑같음. <- 이거 ? 어떰?

- 1:1 과외, 좋은 학원, 1타강사 너무 좋지 -> 이거 고비용 기회 불평등 
	- 수요 공급 불균형 누구나 다 뛰어난 교사는 아니잖아?
	- 이거 해결법 : 툴. 툴 . 툴. 툴 . 등으로 풀었는데,  [사진 첨부]
	- 툴들도 다 무료가 아니고, 다 비용이 발생함
	- 요거를 염두에 두고 봐야함

-------------------------서설 끝----------------------------
수학 비서: 디지털 전환 기반 수학 컨텐츠 저작 플랫폼 [사진 추가]
 데이터 처리에서는 결국 비정형 데이터를 정형 데이터 형식으로 만들어준다. 이게 필요한건 당연히, 이게 더 처리하기 편하니까

문제지가 있을떄, 당연히도 해설지도 필요하지.

해설을 작성을 해야된다. <- 선생님은 이걸 하는데,  이걸 해소해줘야하는데...

[시장] 이미 전문 해설을 사람이 작성도 하고있다.

데이터 처리, 데이터베이스 구축 다 비용이 발생함

PM 에서는 수학 교육학을 전공한 사람들이 작업을 하고있다.

무엇을 하고있는가?

1 단계 
	시험지 원본 업로드 
		문제 지문이 어디인지
		문제 형태
		배점
		수식[요게 발목을 잡어]
		-----부가정보
		유형 
		페이지 번호

		를 추출해서 데이터베이스로 넣어야되는데
		
		문제 풀이 한 시험지를 넣으면
		위에거 + 해설?  풀이? 처럼 생긴 건가? 더럽게 된 낙서(사실 풀이임)가 추가된 시험지에서 원하는 글씨만 읽어올 수 있을까?

		이 시험지에서 어떤 글씨는 취하고 어떤 글씨는 버리고 를 선택 할 수 있을까?

		문제 영역 구분이라는 처리를 해버려. -> 욜로 기반으로 해버려

		이 안에서, 질문 그래프, 선지 이런거 다 구분 해버려 [사진 첨부]

		왜 잘되지? 안될거 같은데?

		-> 압도적인 데이터가 키인거 같다.

		인사이트 : 사람이 해설도 하고 사람이 영역도 잡고 하면서, 미세조정된 욜로겠네...
		프로세스 상에서 자동으로 레이블링이 되었을거아

		모델에 너무 많은 데이터는 오히려 성능을 떨어트릴 수 있음 ( 이건 그냥 ML/DL 이론이지)

		Data 에 bias 가 있을것이다. 학습에 성능이 나오지 않을 수 있지

		낙서가 많은게 일부 사례이면, 낙서가 많은 사진을 아무리 모아서 낙서에 학습을 시키면, 그거에 대한 성능이 그렇게 안올라갈거야

		Tip : augraphy 라는 툴을 써서, augmentation 진행 (document augemnting 잘함)
	
		OCR 에서 synthetic data 를 많이 생성하기도 하지?

		적절히 조합해서 사용하도록.

--------데이터 구조
			위에 첨부한 이미지 처럼 바운딩 박스가 나올텐데, 

			이걸 데이터 구조화 시켜버려.

		Image normalization 등등 다 해야지?

		Text detection / Recognition / -> Restructuring

		[이미지 첨부]
		Scene text detection model -> 예시 머머 있었는데 기억안남
		Segment map -> convext 찾기, contour 찾기, crop 가능한 polygon 좌표 찾기, word polygon
		이미지에서 threshold 찾아야되는데, 바운딩 박스 shrink 등
		hyper param 튜닝이 중요한 문제가 됨 <- 요거 질문좀 해봐야지

		이미지 crop 하고, 텍스트 레커그니션 수행
		비전 인코더 -> text decoder 

		Resent, swinTF

		문제에 맞는 text decoder 학습 당연히 필요하죠

	
2 단계
	아직은 해결하지 못한 문제들...
	
	in Doc OCR -> 
	-> Latex OCR model

	Text Decoder -> Latex 잘 말해야되는데... 
	그냥 a 다 랑 latex 문법상 a 이다 를 나눠야한다.

	YOLO detector 솔직히 삐뚜루 되는 경우 많은데, 이거 어케 fix 할껀지 정해야됨	

	모델이 별개면 다시 학습을 해야되나?

	NAVER DEER 라는 모델 -> End to End 로 OCR 학습 시키는 모델

	텍스트 중앙점을 레커그니션 모델에 전달, 
	
3단계
	doc layout analysis
	
	upstage, naver clova
		
	text 기반 인식, image 기반 인식 

	-> 구조화가 되어야, 된다.

	인식한 텍스트가 무엇인지, 키 밸류로 꾸릴 수 있는지, 그룹바이로 묶어야 하는 데이터인지, 확실히 해야됨
	
	bbox 가 있고, 텍스트가 있다. -> 이걸 아이텀이 뭐고, 네임이 뭐고, structure information 장표 확인

	Image 와 text embedding 이 함께 들어가 있어요

	용도에 따라서, 달라짐... 놓침 ㅋ

	<vqa> 라는 부분도 있는데, 이거 공부 ㄱ

	잘 학습된 LLM 모델은 이런 역할을 해줄 수 있는데,

	헤비한 모델은 학습에 대한 코스트 올라가고, 인퍼런스 비용도 올라감
	
	shallow 한 모델들을 쓰도록 변경을 해서 많이들 트라이 하는중

향후
	LLM -> LMM 
	또 LMM 으로 얘기를 돌리노...
	근데 수학에서 필요함 -> 데이터 구축하고 전문 해석을 사람이 해주고 있는데, 지피티가 많이 도와주겠구나 싶은데, 사실 돌려봤을때, 그렇게 만족스럽지 않다.

	이미지를 주고, 이 문제를 풀고 해설해줘, 완벽한 멀티모달과 차이가 있었어서, OCR -> LMM 탔는데,

	이미지 -> 지시 사항에 대한 답을 주는데,

	이미지임에도 불구하고 OCR 없이 풀어버림.
	
	ㅋ	근데 잘 풀어놓고는 답을 잘 못고름, 언어를 이해하는 능력에는 약간의 오해가 있음

	현업에서 쓰기엔 무리가 있다. 
	
	전문 해설 은 잘 정제된 패턴화된 해설이 효율이 더 높다고 판단한다.

	이게 왜 멀티 모달이 되어야 하느냐, OCR 로는 왜 안되느냐
	
	당연히 그림이 들어가니까. 

	잘 풀어보이기는 하지만, 지피티도 아직은 틀린다.
	
	이런 시도를 하는 사람은 없나.
	더러 많이 있는거 같은데, gemma 도 있고, 캐글에서도 대회를 열었다. AI 로 수학 문제 올림피아드 열었다.
	Latex 형식으로 된 비공개 110개 문제를 가지고 대회를 열었는데, 

	중국 고등학교 수학 수준의 문제

	대회 결과가 1등이 29점

	즉, 31점 

	아직은 한계가 있다.

	물론 모델이 깊어지고 파라미터가 많아지면 더 잘 할거 같긴한데,

	보통은 70B 아래에서 많이들 제출을 했다.

	Gemma 7B 는 3/50 의 성능을 보임

ISSUE : 수학은 말뭉치를 통해서, 찍어맞추기를 할 수 없다.
	Prob solving : 1등 팀 어프로치는, 이 문제를 Sympy 로 계산 할 수 있도록 코드를 짜라.로 만들고
	풀이를 할 수 있는, 답을 얻을 수 있는 문제를 뽑아내고
	에이전트가 문제를 풀어서 실행한 결과를 출력한다.

	ToRA 라는 아이디어

	

	





		