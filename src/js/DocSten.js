var myDocHtml = document.implementation.createHTMLDocument("myDocHtml")
//implementation.createHTMLDocument("not");



/**
 * 
 * @param {String} line     a line in the .md file
 * @returns {Boolean}       the truth on title nature of the line
 * 
 */
function isTitle(line) {
    return line.startsWith("#");
}

/**
 * 
 * @param {String} line     a line in the .md file
 * @returns {Number}        the level of the title in html
 */
function titleLevel(line) {
    let startsLine = line.substring(0,6);
    return countChar(startsLine, "#");
}

/**
 * 
 * @param {Numnber} level 
 * @returns {HTMLTitleElement}
 */
function createTitle_(level) {
    let tagName = "h"+level;

    return myDocHtml.createElement(tagName);
}


function createTitle(lineOrLevel) {
    let argType = typeof lineOrLevel;
    if(argType === "string"){
        if(isTitle(lineOrLevel)){

            let level = titleLevel(lineOrLevel);
            let myTitle = createTitle_(level);
            //innerText_ = myTitle.innerText || myTitle.textContent || ''; // to make more compatible
            //innerText_ = lineOrLevel.slice(level);
            myTitle.textContent = lineOrLevel.slice(level);
            return myTitle;
        }
    }
    else if(argType === "number"){
        return createTitle_(lineOrLevel);
    }
}


/**
 * 
 * @param {String} string a character String
 * @param {Char} char a character
 * @returns {Number} the number of char in string
 */
function countChar(string, char) {

    let count = 0

    Array.from(string).forEach(element => {
        if (element === char)   count++;
    });

    return count;
}












//_________________TEST__________________



//console.log(isTitle("#djiojiz"));
//console.log(createTitle("#djiojiz"));