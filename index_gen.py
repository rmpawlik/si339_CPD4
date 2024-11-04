import os

def create_homepage(meets_folder):
    # Define the homepage filename
    homepage_filename = os.path.join(meets_folder, 'index.html')

    # Get a list of all HTML files in the meets folder
    html_files = [f for f in os.listdir(meets_folder) if f.endswith('.html') and f != 'index.html']
    
    if not html_files:
        print(f"No HTML files found in folder: {meets_folder}")
        return

    # Start building the HTML content for the homepage
    homepage_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meet Results</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/97514ed53b.js" crossorigin="anonymous"></script>
</head>
<body>
    <a href = "#main">Skip to Main Content</a>
    <nav>
      <ul>
         <li> <i class="fa-solid fa-person-running" aria-label="Running icon"> </i></li>
         <li><a href="https://aaskylineathletics.com/" tabindex=0>Skyline High School Athletics</a></li>
      </ul>
    </nav>
    <header>
        <h1>Meet Results Homepage</h1>
        <p>Welcome to the results of the cross-country meets. Select a meet to view details.</p>
         <span class="skyline-logo"><img src="images/AASKYLINELOGO.png" alt="Logo picture of Skyline High School"> </span>
    </header>
    <main>
        <section class="homepage">
            <h2>Available Meets</h2>
            <ul class="meets">
    """

    # Add list items for each HTML file
    for html_file in html_files:
        # Remove the ".html" extension to display a cleaner name
        meet_name = os.path.splitext(html_file)[0]
        # Add a link to the HTML file
        homepage_content += f'                <li><a href="meets/{html_file}">{meet_name.replace("_", " ").title()}</a></li>\n'

    # Close the HTML structure
    homepage_content += """
            </ul>
        </section>
    </main>
    <footer>
        <p>Skyline High School</p>
        <address>
            2552 North Maple Road, Ann Arbor, MI 48103<br>
            <a href="https://www.instagram.com/a2skylinexc/" aria-label="Instagram"><i class="fa-brands fa-instagram"></i> Follow us on Instagram</a>
        </address>
    </footer>
</body>
</html>
"""

    # Write the homepage content to the index.html file
    with open(homepage_filename, 'w', encoding='utf-8') as homepage_file:
        homepage_file.write(homepage_content)

    print(f"Homepage '{homepage_filename}' created successfully.")

if __name__ == "__main__":
    # Define the path to the meets folder
    meets_folder = os.path.join(os.getcwd(), "meets")

    # Check if the meets folder exists
    if not os.path.exists(meets_folder):
        print(f"Folder '{meets_folder}' does not exist.")
    else:
        create_homepage(meets_folder)