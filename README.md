# Number-to-words-conversion-using-bento

### **Procedure to Run Number-to-Words Conversion Using Bento & Flask**  

This guide walks you through setting up and running the pipeline using Bento and Flask.  

---

## **Step 1: Install Dependencies**  
Ensure you have the required dependencies installed.  

```bash
pip install flask num2words pyyaml
```

Download and install **Bento** from [Bento's official site](https://warpstreamlabs.github.io/bento/docs/guides/getting_started#install).  

---

## **Step 2: Create Required Files**  

### **1. Create the API (`api.py`)**  

### **2. Create the Configuration File (`config.yaml`)**  

### **3. Create the Bento Pipeline (`fetch_data.yaml`)**  

---

## **Step 3: Run the Flask API**  
Start the API server in a terminal:  

```bash
python api.py
```

It should start on `http://127.0.0.1:5000`.

---

## **Step 4: Run the Bento Pipeline**  
In a separate terminal, run the Bento pipeline:  

```bash
bento -c ./fetch_data.yaml
```

---

## **Step 5: Verify the Output**  
Check if `output.json` contains the expected result:  

```json
{"words":"twenty-six"}
```

---

## **Step 6: Debugging & Error Handling**  

- **If `config.yaml` is missing or invalid** → The API will return an error.  
- **If the API is not running** → Bento will fail to send the request.  
- **If `output.json` is empty** → Ensure the API is returning the correct response by testing:  

  ```bash
  curl http://127.0.0.1:5000/data
  ```

---

### **Expected Outcome**  
This procedure ensures that:  
- Reads a number from `config.yaml`.  
- Sends it to the Flask API for conversion.  
- Writes the `words` field in `output.json` using Bento.  
