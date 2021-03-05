// class Car {
//   constructor (brand, style) {
//     this.make = brand;
//     this.model = style;
//     // this.year = year;
//     // this.color = color
//   }

//   vehicleName() {
//     return this.make + this.model
//   }

//   // vehicleType() {
//   //   let carYear = this.year
//   //   if (carYear >= 2000) {
//   //     return `Your ${carName} is a classic car`
//   //   }
//   // }

//   // vehicleColor() {
//   //   if 
//   // }
// }


// console.log(myCar)

// // year, color 2005, "white"


class Car {
    constructor(brand) {
      this.carname = brand;
    }
    present() {
      return 'I have a ' + this.carname;
    }
  }
  
  let myCar = new Car ('toyota')
  console.log(myCar)