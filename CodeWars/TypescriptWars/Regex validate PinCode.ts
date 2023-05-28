
// write a function that checks if a pin code is 4 or 6 digits long and contains only integers
// return true if both cases are true, return false otherwise.

  export function validatePin (pin: string): boolean {
    if (pin.length === 4 || pin.length === 6) {
      if (/^[0-9]+$/.test(pin)) {
        return true
      }
    }
    return false
  }

