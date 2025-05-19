# ChatGPT Beadandó

A program tesztelhető a "https://chatgptbeadando.vercel.app/" címen. Mivel a backend a Render segítségével van hostolva, sokszor lassan válaszol az első kérdésre.

## Backend helyi teszteléshez
```
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt 
uvicorn main:app --reload
```
```
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question": "What is LangChain?"}'
```

### RAG teszt

#### prompt
``` When was the first electric guitar made? ```

#### válasz
``` The first electric guitar was made in 1931. ```


### Internetes kereső teszt

#### prompt
``` What's the weather like in Pécs currently? ```

#### válasz
``` The weather in Pécs currently is 63°F with mostly sunny skies. ```


### LLM teszt

#### prompt
``` How are you? ```

#### válasz
``` I am fine, thank you! ```

