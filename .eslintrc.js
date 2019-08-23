// All rules explained here: http://eslint.org/docs/rules/
// Controlling rules:
//   "rule-name": 0 // disable rule
//   "rule-name": 1 // enable rule as a warning
//   "rule-name": 2 // enable rule as an error

// Also:
//   "rule-name": [2, 'always'] // enable rule as error, with the option 'always'
//   "rule-name": [2, { boolean: false, awesome: true }] // enable rule as error, with an object for the options
module.exports = {
    extends: [
        "plugin:vue/recommended",
        "airbnb-base"
    ],
    rules: {
        'indent': [1, 4],  // warnings-only, 4-space indents.
        'semi': [2, "always"],
        'no-console': 1,  // warn on console logs
        'linebreak-style': 0,  // allow CRLF and LF
        'max-len': 1, // warn on length > 100
        'no-restricted-globals': 1, // is flagging location, but no clear alternative
    },
    env: {
        node: true,
        es6: true,
        browser: true,
        jquery: true
    },
    globals: {
        Vue: false,
        axios: false,
    }
};
