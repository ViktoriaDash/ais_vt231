"""
====================================================================
ІНСТРУКЦІЯ З ІНСТАЛЯЦІЇ ТА ЗАПУСКУ:
1. Встановіть бібліотеку для роботи з API: pip install openai
2. Переконайтеся, що Ollama завантажена та запущена: ollama serve
3. Завантажте рекомендовану модель: ollama pull qwen3:1.7b
4. Запустіть застосунок: python app.py
====================================================================
"""

import sys
from openai import OpenAI

try:
    client = OpenAI(
        base_url="http://localhost:11434/v1", 
        api_key="local"
    )
    MODEL_NAME = "qwen3:1.7b"
except Exception as e:
    print(f"[ПОМИЛКА] Не вдалося ініціалізувати клієнт OpenAI: {e}")
    sys.exit(1)

print("="*60)
print("🎓 AI-ГЕНЕРАТОР КАРТОК (FLASHCARDS) ДЛЯ КВІЗУ")
print("Теми: кіно, актори, страви, країни, музичні гурти тощо.")
print("="*60)

while True:
    print("\nВведіть тему для квізу (або 'q' для виходу):")
    topic = input("> ")
    
    if topic.lower() == 'q':
        print("Хай щастить на квізі! До зустрічі!")
        break
    
    if not topic.strip():
        print("Будь ласка, введіть коректну тему.")
        continue
        
    full_prompt = (
        f"Створи рівно 5 чітких і реальних карток для квізу на тему '{topic}' українською мовою. "
        "Пиши виключно грамотною українською мовою, без вигаданих термінів. "
        "Використовуй строго такий формат для кожної картки:\n"
        "Питання: [Текст питання]\n"
        "Відповідь: [Текст відповіді]\n"
    )
    
    print("\nГенерація карток...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7,
            max_tokens=1200,
            stream=False
        )
        
        print("-" * 50)
        content = response.choices[0].message.content
        
        if content and content.strip():
            print(content)
        else:
            print("[УВАГА] Модель повернула порожню відповідь. Спробуйте ввести тему ще раз.")
            
        print("-" * 50)
        
    except Exception as e:
        print(f"\n[ПОМИЛКА СЕРВЕРА] Не вдалося отримати відповідь. Деталі: {e}")