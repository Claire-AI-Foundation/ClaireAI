
export default {

  /**
   * Get a color base on a string input.
   * @param {String} str - string input
   * @return A string representing the color (e.g. "yellow")
   * @author Godwin Gabriel
   */
  colorMinder (str) {
    const char = typeof str === 'string' ? str.charAt(0) : 'ff'
    const groups = ['a', 'b', 'c', 'd', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
      'e', 'f', 'g', 'h', 'u', 'v', 'w', 'x', 'i', 'j', 'k', 'l', 'y', 'z']
    const charIndex = groups.indexOf(char.toLowerCase()) + 1

    return charIndex <= 4 ? 'teal'
      : charIndex <= 8 ? 'purple'
        : charIndex <= 12 ? 'success'
          : charIndex <= 18 ? 'primary'
            : charIndex <= 24 ? 'orange'
              : 'primary'
  },
  capitalize (text) {
    return text ? text.toLowerCase().split(' ')
      .map(w => w.substring(0, 1).toUpperCase() + w.substring(1)).join(' ') : text
  },
  truncateText (text, length = 18) {
    if (typeof text !== 'string') return

    // strip all line breaks
    const regexp = /\n/g
    text = text.replace(regexp, ' ')

    return text.length > length
      ? text.substr(0, length) + '...' : text
  },
  copyToClipboard (text) {
    if (window.clipboardData && window.clipboardData.setData) {
      // IE specific code path to prevent textarea being shown while dialog is visible.
      return window.clipboardData.setData('Text', text)
    } else if (document.queryCommandSupported && document.queryCommandSupported('copy')) {
      var textarea = document.createElement('textarea')
      textarea.textContent = text
      textarea.style.position = 'fixed' // Prevent scrolling to bottom of page in MS Edge.
      document.body.appendChild(textarea)
      textarea.select()
      try {
        return document.execCommand('copy') // Security exception may be thrown by some browsers.
      } catch (ex) {
        // console.warn("Copy to clipboard failed.", ex);
        return false
      } finally {
        document.body.removeChild(textarea)
        // return true
      }
    }
  },
  getRandomString (len = 8) {
    let text = ''
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for (let i = 0; i < len; i++) { text += possible.charAt(Math.floor(Math.random() * possible.length)) }

    return text
  },
  getRandomNumber (len = 6) {
    let num = ''
    const possible = '0123456789'

    for (let i = 0; i < len; i++) { num += possible.charAt(Math.floor(Math.random() * possible.length)) }

    return num
  },
  generateUUID () { // -- StackOverflow
    var d = new Date().getTime()// Timestamp
    var d2 = (performance && performance.now && (performance.now() * 1000)) || 0// Time in microseconds since page-load or 0 if unsupported
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16// random number between 0 and 16
      if (d > 0) { // Use timestamp until depleted
        r = (d + r) % 16 | 0
        d = Math.floor(d / 16)
      } else { // Use microseconds since page-load if supported
        r = (d2 + r) % 16 | 0
        d2 = Math.floor(d2 / 16)
      }
      return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16)
    })
  },

  parseDate (timestamp, showDate = false) {
    // showDate is used to control which type of date to return - full date or only time
    // USING CLIENT TIME. MAYBE USE SERVER TIME ?
    // handle firebase timestamp object
    timestamp = typeof timestamp === 'object' ? timestamp.toMillis() : timestamp

    const d = new Date(timestamp)
    const now = Date.now()
    const diff = now - timestamp

    const oneSec = 1000
    const oneMin = oneSec * 60
    const oneHour = oneMin * 60
    const oneDay = oneHour * 24

    const options = { hour: 'numeric', minute: 'numeric' }
    const options2 = {
      day: 'numeric',
      year: 'numeric',
      month: 'short',
      hour: 'numeric',
      minute: 'numeric'
    }

    if (diff < 1000) {
      return 'just now'
    }
    if (diff > oneSec && diff < oneMin) {
      return 'a few seconds ago'
    }
    if (diff > oneMin && diff < oneHour) {
      return Math.floor(diff / oneMin) + ' minutes ago'
    }
    if (diff >= oneHour && diff < 2 * oneHour) {
      return 'an hour ago'
    }
    if (diff > oneHour && diff < oneDay) {
      return Math.floor(diff / oneHour) + ' hours ago'
    }
    if (diff > oneDay && diff < oneDay * 2) {
      return 'yesterday, ' + d.toLocaleString('en-US', options)
    }
    if (diff >= oneDay * 2 && diff < oneDay * 3) {
      return '2d ago at ' + d.toLocaleString('en-US', showDate ? options2 : options)
    }
    return d.toLocaleString('en-US', showDate ? options2 : options)
  },
  imageToBase64 (file) {
    return new Promise((resolve, reject) => {
      var reader = new FileReader()
      reader.onloadend = () => resolve(reader.result)
      reader.onerror = reject
      reader.readAsDataURL(file)
    })
  }

}
