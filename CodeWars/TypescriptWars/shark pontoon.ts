export function shark(pontoonDistance: number, sharkDistance: number, youSpeed: number, sharkSpeed: number, dolphin: boolean): string {

    while(true){
        if (dolphin){
            pontoonDistance -= youSpeed
            sharkDistance -= (sharkSpeed / 2)
        }
        else {
            pontoonDistance -= youSpeed
            sharkDistance -= sharkSpeed
        }

        if (pontoonDistance <= 0 && sharkDistance <= 0){
            return 'Shark Bait!'
        }
        if (pontoonDistance > 0 && sharkDistance <= -pontoonDistance){
            return 'Shark Bait!'
        }
        if (pontoonDistance <= 0 && sharkDistance > 0){
            return 'Alive!'
        }
    }
}

export function sharky(pontoonDistance: number, sharkDistance: number, youSpeed: number, sharkSpeed: number, dolphin: boolean): string {
  let shark_ = sharkDistance / sharkSpeed
  let you_ = pontoonDistance / youSpeed
  if (dolphin){
    shark_ = sharkDistance / (sharkSpeed / 2)
  }

  return shark_ > you_? 'Alive!' : 'Shark Bait!'
}




