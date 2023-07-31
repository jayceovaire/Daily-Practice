// Your online store likes to give out coupons for special occasions. Some customers try to
// cheat the system by entering invalid codes or using expired coupons.
// Your mission:
// Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
// A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
export function checkCoupon(enteredCode: string, correctCode: string, currentDate: string, expirationDate: string): boolean {
    const currentDateObj = new Date(currentDate);
    const expirationDateObj = new Date(expirationDate);

    return enteredCode === correctCode && currentDateObj <= expirationDateObj;
}
