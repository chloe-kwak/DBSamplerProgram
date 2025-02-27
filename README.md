# DB Sampler Program

DB Sampler Program은 AWS의 주요 데이터베이스 서비스들을 실습을 통해 경험해볼 수 있는 워크샵 프로그램입니다. <br>비어 샘플러처럼 다양한 데이터베이스를 맛보고 각각의 특징과 장단점을 이해할 수 있도록 구성되었습니다.

## 개요

이 프로그램은 온프레미스 환경에서 상용 데이터베이스(주로 Oracle)를 사용하는 고객들이 AWS 클라우드로 마이그레이션할 때, 워크로드 특성에 맞는 최적의 데이터베이스를 선택할 수 있도록 도와주는 것을 목표로 합니다.

## 제공되는 데이터베이스 워크샵

### 1. DynamoDB
- NoSQL 데이터베이스
- 빠른 읽기/쓰기가 중요한 워크로드 (예: 쇼핑카트, 상품 카탈로그)
- 실습 내용:
  - 레스토랑 정보 관리 애플리케이션
  - 테이블 생성 및 데이터 로드
  - 리뷰 시스템 구현

### 2. Neptune
- 그래프 데이터베이스
- 복잡한 관계 데이터 분석 및 생성형AI GraphRAG의 Vector Store
- 실습 내용:
  - 의심스러운 IP 주소 탐지
  - 사용자 관계 분석
  - 그래프 데이터 로드 및 쿼리

### 3. OpenSearch
- 검색 엔진
- 전문 검색, 로그 분석 및 생성형AI RAG의 Vector Store
- 실습 내용:
  - IMDB 데이터 인덱싱
  - IMDB 데이터 쿼리

### 4. Redis (ElastiCache)
- 인메모리 캐시
- 밀리세컨드 이하 응답 시간이 필요한 워크로드
- 실습 내용:
  - 캐싱 시스템 구현
  - 레스토랑 정보 조회 성능 개선
  - 연결 테스트

## 디렉토리 구조

각 데이터베이스 워크샵은 다음과 같은 구조로 구성되어 있습니다:

```
데이터베이스명/
├── *.ipynb          # Jupyter 노트북 실습 가이드
├── requirements.txt  # 필요한 Python 패키지
├── application/     # 샘플 애플리케이션 코드
├── scripts/         # 유틸리티 스크립트
└── img/            # 실습 가이드 이미지
```

## 시작하기

### 방법 1: CloudFormation을 통한 자동 설정 (권장)

1. CloudFormation 스택 생성:
   - AWS 콘솔에서 CloudFormation 서비스로 이동
   - 'Create stack' > 'With new resources (standard)' 선택 > Specify template에서 'Upload a template file' 선택
   - 'db-sampler-cf-template.yaml' 파일 업로드
   - 스택 이름 입력 후 생성

2. 생성되는 리소스:
   - SageMaker 노트북 인스턴스 (ml.t3.xlarge)
   - 필요한 IAM 역할 및 권한
     * DynamoDB 접근 권한
     * Neptune 접근 권한
     * OpenSearch 접근 권한
     * ElastiCache 접근 권한
     * S3 접근 권한
     * SageMaker 관련 권한

3. 자동 설정 완료:
   - 노트북 인스턴스가 생성되면 자동으로 실습 자료가 다운로드됨
   - 노트북 인스턴스의 'Open JupyterLab' 클릭하여 실습 시작

### 방법 2: 수동 설정

1. Amazon SageMaker AI의 JupyterLab 환경 설정:
   - JupyterLab에서 터미널을 엽니다.
   - SageMaker 디렉토리로 이동:
   ```bash
   cd SageMaker
   ```
   - 실습 자료 다운로드:
   ```bash
   git clone https://github.com/chloe-kwak/DBSamplerProgram.git
   ```

2. 필요한 패키지 설치:
```bash
cd DBSamplerProgram

pip install -r requirements.txt -U
```

3. 노트북의 지시사항을 따라 실습을 진행합니다.
- Amazon SageMaker AI의 Notebook (JupyterLab) 에서 실습 합니다.

## 참고사항

- 각 워크샵은 독립적으로 실행 가능합니다.
- 실습을 위해서는 AWS 계정과 적절한 권한이 필요합니다.
- 자세한 내용은 각 데이터베이스 디렉토리의 노트북 파일을 참조하세요.
- CloudFormation 스택 삭제 시 생성된 모든 리소스가 자동으로 제거됩니다.
