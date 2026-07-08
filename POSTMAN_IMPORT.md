# Postman Collection Import Guide

## Quick Steps

1. **Open Postman** (desktop app or web version)

2. **Click "Import"** button in the top-left corner

3. **Upload the file:**
   - Drag and drop `postman_collection.json` into the window
   - OR click "Choose Files" and select the file

4. **Click "Import"** to confirm

5. **Set base URL** (if needed):
   - Click on the collection name
   - Go to "Variables" tab
   - Verify `base_url` = `http://127.0.0.1:8000`

6. **Start testing:**
   - First, run "Login and Get Token" request
   - Token will be saved automatically
   - Use other endpoints with authentication

Done! Your API collection is ready to use.
