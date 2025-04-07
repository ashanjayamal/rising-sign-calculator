# Rising Sign Calculator

A web-based astrological tool that calculates your Rising Sign (Ascendant) based on your birth details.



## 🌟 About

The Rising Sign Calculator determines the zodiac sign that was rising on the eastern horizon at the time of your birth. In astrology, the Rising Sign (or Ascendant) influences your outward style, appearance, and how others perceive you upon first meeting.

## ✨ Features

- Calculate your Rising Sign based on:
  - Birth date
  - Birth time
  - Latitude and longitude of birth location
  - Timezone
- Display zodiac sign images
- User-friendly interface with responsive design
- Works entirely in the browser (no server-side calculations)

## 🔧 Technical Implementation

This calculator uses astronomical principles to determine the Rising Sign:

1. Calculates Local Sidereal Time (LST) at birth
2. Determines the ascendant degree based on LST and birth location
3. Maps the ascendant degree to the corresponding zodiac sign

The calculation is based on astronomical formulas implemented in JavaScript, including:
- Julian date conversion
- Greenwich Mean Sidereal Time calculation
- Local Sidereal Time calculation
- Ascendant degree calculation

## 🚀 Getting Started

### Visit the Live Website
You can use the calculator directly at: [https://ashanjayamal.github.io/rising-sign-calculator/](https://ashanjayamal.github.io/rising-sign-calculator/)

### Run Locally
To run this project locally:

1. Clone the repository:
   ```
   git clone https://github.com/ashanjayamal/rising-sign-calculator.git
   ```

2. Open `index.html` in your web browser.

No additional dependencies or installation is required!

## 📝 Usage Instructions

1. Enter your birth date
2. Enter your birth time (24-hour format)
3. Enter the latitude and longitude of your birth location
   - You can find these coordinates using Google Maps or similar tools
4. Select your birth location's timezone
5. Click "Calculate Rising Sign"
6. View your Rising Sign result with its corresponding zodiac image

## 📜 Background

This project was inspired by astrological principles and uses a simplified version of the astronomical calculations used by astrologers to determine rising signs. The original concept was implemented in Python using the Astropy library, and has been adapted for web use with JavaScript.

## 📱 Compatibility

The Rising Sign Calculator works on:
- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Mobile devices
- Tablets

## 📸 Image Credits

The zodiac sign images used in this project are stored in the `images` directory.

## 🔮 Future Enhancements

Planned features for future versions:
- Location search functionality using a geocoding API
- More detailed descriptions for each Rising Sign
- Additional astrological calculations (Moon Sign, Sun Sign, etc.)
- Birth chart visualization
- More accurate astronomical calculations



## 🙏 Acknowledgements

- Astronomical calculation principles from the Astropy Python library
- Zodiac sign imagery adapted for web use



---

Created with ❤️ by ashanjayamal
