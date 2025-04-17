# Gemini Chatbot

## Mô tả
Chatbot đơn giản sử dụng Google Gemini API và FastAPI.

## Cài đặt & chạy local

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your_real_key"
uvicorn main:app --reload
```

Truy cập http://localhost:8000

## Deploy lên Render
- Tạo web service mới
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host=0.0.0.0 --port=10000`
- Env: `GEMINI_API_KEY=your_key`
