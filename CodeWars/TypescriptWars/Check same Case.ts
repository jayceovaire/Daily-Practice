
// given two strings of a single character, check if both characters are the same case, if they are return 1
// if not return 0
// if either of the arguments are not letter characters return -1

export function sameCase(a: string, b: string): number {

  const isLetter = (char: string): boolean => /[a-zA-Z]/.test(char);

  if (!isLetter(a) || !isLetter(b)){
    return -1
  }
  if (/[a-z]/.test(a) == true && /[a-z]/.test(b) == true){
    return 1
  }
  if (/[A-Z]/.test(a) == true && /[A-Z]/.test(b) == true){
    return 1
  }
  else {
    return 0
  }

}



