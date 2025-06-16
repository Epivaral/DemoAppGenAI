# CopilotPrompt.md

## Project: Personal Book Library with Azure Static Web Apps, Blazor, and Data API Builder

This file summarizes the key steps and prompts from a real GitHub Copilot Chat session, showing how to build a full-stack demo with Blazor, Azure Static Web Apps, and Data API Builder. Use this as a learning resource for your own projects!

---

### 1. Ask ChatGPT for ideas for a simple web app:

**Prompt:**
> Give me ideas for a simple web app using static web apps in azure, most for learning and teaching, a simple CRUD with just one table in azure SQL DB






### 2. Create the Books Table and Sample Data

**Prompt:**
> @mssql Personal Book Library
>
> Table: Books
> Columns: BookID, Title, Author, Genre, ReadStatus
>
> Please generate the CREATE TABLE statement and then insert 20 book records on it
>
> please generate the .sql files on a new folder called DABATASE
>
> generate the DROP TABLE command if te table exists in the same file as the CREATE statement

**Issue & Solution:**
- No major issues. The table and insert scripts were generated and placed in the correct folder as requested.

---

### 3. Add Book Description Field

**Prompt:**
> update the table and the records to include book description field

**Issue & Solution:**
- The schema and insert statements were updated to include a `Description` field for each book. No issues encountered.

---

### 4. Create a Blazor WebAssembly App for Azure Static Web Apps

**Prompt:**
> Create a Hello world web site for Azure Static web apps.
>
> I want a simple page to display hello world message
>
> Static web app must use blazor and please create all the required folders and files so it can be properly deployed to azure using action file (See <attachments> above for file contents. You may not need to search or read the file again.)

**Issue & Solution:**
- Initial build failed due to missing `.csproj` file. Solution: Generated a minimal Blazor project file and ensured the folder structure matched the GitHub Actions workflow.
- Fixed missing `HttpClient` registration and other minor Blazor setup issues.

---

### 5. Configure GitHub Actions for Azure Static Web Apps

**Prompt:**
> update the YML action file to point to the new fonders created

**Issue & Solution:**
- The workflow was not finding the build output. Solution: Updated `app_location` and `output_location` to match the new Blazor app structure.

---

### 6. Add Data API Builder Configuration

**Prompt:**
> generate a new folder swa-db-connections in the root folder of the repo, and to create a swa-db-connections/staticwebapp.database.config.json file for data api builder for the books table we created
>
> Make sure it works with static web apps

**Issue & Solution:**
- The config schema and structure needed to match Azure Data API Builder requirements. Solution: Used the correct schema and included all required sections (`runtime`, `host`, `entities`).

---

### 7. Display Books from the API in Blazor

**Prompt:**
> using the API we created, and is located at https://lemon-pebble-088965b1e.1.azurestaticapps.net/data-api/api/Books
>
> can you please update Blazor App to display the books as a table, add a header that says "My Personal Book collection"

**Issue & Solution:**
- The API response format was `{ "value": [...] }`, not a plain array. Solution: Adjusted the deserialization logic to match the actual API response.
- Fixed issues with missing or misconfigured `HttpClient` registration in Blazor.

---

### 8. Style the Blazor App

**Prompt:**
> can you please update my website style to look like this picture, format the table and the background of the site, also format the header.
>
> Please do not change anything on how the api is called, as is working as expected, only update the style and colors

**Issue & Solution:**
- No major issues. Added modern CSS for background, table, and header to improve the look and feel.

---

### 9. Generate Book Cover Images with Azure OpenAI

**Prompt:**
> can you please update the file, so it can iterate over all books, in this api:
>
> https://witty-smoke-0cafe3b1e.6.azurestaticapps.net/data-api/api/Books
>
> the api will provide the prompt for Title, Genre and description
>
> save the generated images to the images folder

**Issue & Solution:**
- The API response was wrapped in a `value` property. Solution: Extracted the list from `books["value"]`.
- Some prompts triggered OpenAI's content policy. Solution: Added error handling to skip books that fail and continue processing the rest.

---

### 10. Display Book Cover Images in the Table

**Prompt:**
> can you update the table to display the images generated on the images folder? each book with its image, if there is no image, then just leave the cell blank

**Issue & Solution:**
- Blazor WebAssembly cannot check for file existence on the server. Solution: Used the `onerror` attribute in the `<img>` tag to hide images that fail to load.

---

### 11. Use Checkboxes for Read Status

**Prompt:**
> please update the read status to use checkboxes instead of the word

**Issue & Solution:**
- Replaced the text with a disabled checkbox, checked if the book is marked as "read".

---

### 12. Add Update Functionality

**Prompt:**
> Can you make the checkboxes updatable, and use the same API to update the read status, also a SAVE button above the table.

**Issue & Solution:**
- Initial attempts to update only changed books caused issues with Blazor's binding and dirty tracking. Rolled back to updating all books on SAVE for reliability.
- Fixed API payload to only send allowed fields and correct case for `ReadStatus`.
- Used a foreach loop for table rendering to avoid Blazor binding errors.
- Ensured checkboxes are editable and SAVE button updates all records.

---

### 13. UI Polish and Sticky Title

**Prompt:**
> 1. can you update the UI so the title is padded at the top of the page.
> 2. make the message: You can update the read status of the books below and click SAVE to apply changes, and SAVE buttom to be aligned with the table.
> 3. make the SAVE button dark with light text, but different color from the title, but still in armony with overall look

**Issue & Solution:**
- Added extra top padding to the title, then made it sticky at the very top with no padding as requested.
- Aligned the message and SAVE button horizontally with the table using flexbox.
- Styled the SAVE button with a dark color distinct from the title bar, matching the overall look.
- Updated the site title in the browser tab.

---

## How to Use This File

- Each section shows a real user prompt, the resulting feature or change, and how issues were resolved.
- You can follow these steps to build your own Blazor + Azure Static Web Apps + Data API Builder project.
- Use the prompts as inspiration for your own Copilot Chat sessions!

---

Happy learning and building!
