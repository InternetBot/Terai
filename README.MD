# Terminal Recorder + AI Walkthrough Generator  

**Made for my personal use.**  

This tool records my terminal sessions (e.g. while solving HackTheBox labs) and automatically turns them into clean Markdown walkthroughs. No more manually rewriting every step — the AI generates explanations of commands and outputs for me.  

---

## Commands to run 

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
    ```

2. Make the recording script executable:  
   ```bash
   chmod +x terminalRecord.sh
    ```


SIDE NOTE: CREATE YOUR .env file and add this in there 
 ```bash
OPENAI_API_KEY=your-api-key-here
```

## Future Plans  
- Add support for multiple AI models.  
- Smarter chunking for large logs.  
- Pre-clean ANSI escape codes.  
