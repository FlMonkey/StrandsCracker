/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html', ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      'dark', // first one is the default theme
      {
        strandsTheme: { // custom theme
          'primary': '#FFFFFF', // Example color
          'tertiary': '#000000', // Example color
          'secondary': '#AEDFEE', // Example color
          'accent': '#CFCFCF', // Example color
          // define other colors as needed
        },
      },
    ],
  },
}

