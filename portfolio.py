Github present or not 

portfolio_generator_prompt = """
Act as a **Staff Engineer and Lead UX Strategist**. Your task is to generate a **Cinematic, High-Performance, and Recruiter-Ready** portfolio website. The aesthetic must be **Cyber-Minimalist**: highly functional, dark-themed, and exceptionally clear.

Generate a **complete, single-file, responsive** portfolio website.
- CSS MUST be in a <style> tag.
- All JavaScript MUST be in a <script> tag.
- ALL external links MUST open in a new tab (`target="_blank"`).
- Use the provided colors: **Primary Accent: Electric Blue (#00BFFF)**, **Secondary Accent: Cyan (#00E0FF)**, **Deep Background: Dark Charcoal (#121212)**.

**RECRUITER-FOCUSED UI/UX REQUIREMENTS:**

1.  **Aesthetic Foundation (Minimalist Dark):** Use the deep background color. Containers must use subtle **flat drop shadows and border gradients**—**NO NEUMORPHISM**. The focus is on clean lines and high contrast.
    * **Chromatic Aberration:** Apply a subtle `filter: drop-shadow()` effect using the cyan and Electric Blue tones to headings on hover.

2.  **Hero Section & Geometry (CRITICAL CONSOLIDATION):**
    * **Structure:** The main hero section (`<section id="hero">`) MUST contain the **Typewriter Name/Title**. The **Geometry Animation (`tsparticles`)** must be integrated as the hero section's background, appearing in one unified area.
    * **Hero Text (Name):** Text color MUST be **Pure White (`#FFFFFF`)**. Shadow effect must be a **Single, Subtle Electric Blue Glow (#00BFFF)**. NO Glitch effect.
    * **Functional Movement:** The accompanying titles MUST use the **JS Typewriter Effect**.
    * **Navigation Structure (ELIMINATED):** **STRICTLY DO NOT RENDER ANY VISIBLE NAVBAR, HEADER LINKS, OR TOP TITLES.**
    * **Scroll Indicator:** Header MUST include a subtle **Electric Blue Scroll-Progress Indicator Bar** at the top.

3.  **Skills Section (VISUAL EFFECT & LABEL FIX):**
    * **Label Fix:** The Skills section heading MUST be labeled **'Skills'** (using `<section id="skills">`).
    * **Visual Effect:** Individual skill tags/chips MUST have a **soft Electric Blue Glow-on-Hover** effect (`box-shadow` or similar).

4.  **Project Cards (CRITICAL CONDITIONAL REDIRECTION):**
    * **Link Guarantee (Working Redirects):** The external project link button/anchor MUST be present and clickable (opening in a **new tab**) **ONLY IF** the `link` field in the JSON data is present and valid. If the link is missing or empty, the button must be **omitted** or visually disabled (e.g., "Link N/A").
    * **Interaction:** On hover, the project card MUST use **Slight upward translation (`transform: translateY(-8px)`) and a visible border highlight using the Electric Blue Accent**.

5.  **Motion (Clean Animation - Guaranteed):** Sections must use the **AOS/IntersectionObserver** pattern for entrance animations, demanding a **clean, quick fade-in/slide-up**.

6.  **Particles/Geometry (CRITICAL ANIMATION - GUARANTEED):** Integrate `tsparticles` with low count (e.g., 30-50), slow speed, and **mandatory visible Electric Blue connection lines between particles**.

7.  **Contact Section (SIMPLIFIED FOOTER LOGIC):**
    * The contact footer (`<section id="contact">`) MUST clearly display the user's **Email** and **LinkedIn** link.
    * **Conditional Resume Download:** A prominent "Download Resume" button MUST be rendered **ONLY IF** the `resume_data_uri` is present (not empty). If the URI is empty, the button MUST NOT appear.
    * **Section IDs:** The target IDs for all main sections (`about`, `skills`, `projects`, `contact`) **MUST** be present in the HTML to ensure proper internal linking.

---
**DATA (as a JSON object):**
{data_json}
**RESUME (as a Base64 Data URI):**
{resume_data_uri}
---
Generate the complete, single-file HTML. Start with `<!DOCTYPE html>` and end with `</html>`. **The output must be pure, working HTML/CSS/JS.** Do NOT wrap code in markdown backticks.
"""

Redirect Github and title

portfolio_generator_prompt = """
Act as a **Staff Engineer and Lead UX Strategist**. Your task is to generate a **Cinematic, High-Performance, and Recruiter-Ready** portfolio website. The aesthetic must be **Cyber-Minimalist**: highly functional, dark-themed, and exceptionally clear.

Generate a **complete, single-file, responsive** portfolio website.
- CSS MUST be in a <style> tag.
- All JavaScript MUST be in a <script> tag.
- ALL external links MUST open in a new tab (`target="_blank"`).
- Use the provided colors: **Primary Accent: Electric Blue (#00BFFF)**, **Secondary Accent: Cyan (#00E0FF)**, **Deep Background: Dark Charcoal (#121212)**.

**RECRUITER-FOCUSED UI/UX REQUIREMENTS:**

1.  **Aesthetic Foundation (Minimalist Dark):** Use the deep background color. Containers must use subtle **flat drop shadows and border gradients**—**NO NEUMORPHISM**. The focus is on clean lines and high contrast.
    * **Chromatic Aberration:** Apply a subtle `filter: drop-shadow()` effect using the cyan and Electric Blue tones to headings on hover.

2.  **Typography & Hero (Professional Impact):** Integrate 'Inter' or 'Montserrat' from Google Fonts.
    * **Hero Text (Name):** Text color MUST be **Pure White (`#FFFFFF`)**. Shadow effect must be a **Single, Subtle Electric Blue Glow (#00BFFF)**. NO Glitch effect.
    * **Functional Movement:** The accompanying titles MUST use the **JS Typewriter Effect**.
    * **Navigation Bar (CRITICAL FIX - MUST WORK):** The visible navigation bar (`About`, `Skills`, `Projects`, `Contact`) MUST be rendered, and its links MUST use correct, working **smooth scrolling anchor links** (`<a href="#section-id">`) to seamlessly navigate the page.

3.  **Section IDs (CRITICAL ARCHITECTURE):** The main content sections MUST be explicitly defined with the following **matching HTML IDs**: **<section id="about">**, **<section id="skills">**, **<section id="projects">**, and **<section id="contact">**.

4.  **Project Cards (CONDITIONAL REDIRECTION GUARANTEE):**
    * **Interaction:** On hover, the project card MUST use **Slight upward translation (`transform: translateY(-8px)`) and a visible border highlight using the Electric Blue Accent**.
    * **Link Guarantee:** The project link button/anchor MUST be present and clickable (opening in a **new tab**) **ONLY IF** the `link` field in the JSON data is present and valid. **This link takes precedence.** If the link is missing or empty, the button must be omitted or visually disabled (e.g., show "Link N/A").

5.  **Particles/Geometry (IMPROVED ANIMATION - Vortex Effect):** Integrate `tsparticles` with low count (e.g., 40-60), slow speed, **increased opacity/glow**, and **mandatory visible Electric Blue connection lines between particles, simulating a constantly moving, bright geometric data vortex**.

6.  **Contact Section (SIMPLIFIED FOOTER LOGIC):**
    * The contact footer (`<section id="contact">`) MUST clearly display the user's **Email** and **LinkedIn** link.
    * **Conditional Resume Download (CRITICAL):** A prominent "Download Resume" button MUST be rendered **ONLY IF** the `resume_data_uri` is present (not empty). If the URI is empty, the button MUST NOT appear.

---
**DATA (as a JSON object):**
{data_json}
**RESUME (as a Base64 Data URI):**
{resume_data_uri}
---
Generate the complete, single-file HTML. Start with `<!DOCTYPE html>` and end with `</html>`. **The output must be pure, working HTML/CSS/JS.** Do NOT wrap code in markdown backticks.
"""