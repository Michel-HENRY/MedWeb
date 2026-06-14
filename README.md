# MedWeb

An example of a static medical website for a fictional "Centre Médical".
It is built with plain HTML and a single CSS file — no build step, no JavaScript.

## Project structure

```
MedWeb/
├── index.html              # Accueil (home page)
├── notre-centre.html       # Notre centre (care philosophy, locations, photo)
├── consultations.html      # Consultations (centers + doctors, booking links)
├── candidatures.html       # Candidatures (open jobs + apply link)
├── contact.html            # Contact (addresses, phone, email, hours)
├── header.html             # Shared header partial (logo + navigation)
├── footer.html             # Shared footer partial
├── style.css               # Single stylesheet for the whole site
├── images/
│   ├── logo.svg            # Site logo (shown in the header)
│   ├── centre.jpg          # Photo of the center (add this yourself)
│   └── README.txt          # Note about the center photo
├── profiles/
│   └── doctor1.svg … doctor8.svg  # Doctor profile pictures (stickman placeholders)
├── scripts/
│   └── update_partials.py  # Syncs header/footer into every page
├── README.md
└── LICENSE
```

Open `index.html` in a browser to view the site, or serve the folder with
`python3 -m http.server` and visit <http://localhost:8000>.

## Updating the header & footer

The header and footer are shared across all pages. Do **not** edit them page by
page — edit the partials and run the sync script.

1. Edit `header.html` and/or `footer.html` at the project root.
2. Run the sync script from the project root:

   ```bash
   python3 scripts/update_partials.py
   ```

The script replaces the `<header>…</header>` and `<footer>…</footer>` block of
every page with the content of the partials. It also automatically adds
`class="active"` to the navigation link of the current page, so the highlight
stays correct. Re-running the script when nothing changed reports every page as
`unchanged`.

## Where to put the logo

The logo lives at `images/logo.svg` and is referenced by `header.html` as:

```html
<img class="brand-logo" src="images/logo.svg" alt="Logo Centre Médical">
```

To change the logo, replace `images/logo.svg` (keep the same name and path, or
update the `src` in `header.html` and re-run the sync script). Its size is
controlled by the `.brand-logo` rule in `style.css`.

## Color palette

| Color  | Value              | Usage                              |
| ------ | ------------------ | ---------------------------------- |
| Blue   | `rgb(32,102,158)`  | Headings, navigation, specialties  |
| Green  | `rgb(196,214,166)` | Backgrounds, card/hero accents     |
| Orange | `#D9A84E`          | All buttons                        |

## Things to fill in

These are placeholders in the current site:

- **Doctoranytime / booking links** — `href="#"` on the consultation buttons.
- **Google Form** — `href="#"` on the candidature button.
- **Phone & email** — placeholder values in `contact.html`.
- **Center photo** — add `images/centre.jpg`.
