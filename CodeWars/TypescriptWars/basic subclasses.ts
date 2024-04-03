export abstract class Human{};
export class Man extends Human{};
export class Woman extends Human{};

export class God {
    static create(){
        return [new Man(), new Woman()];
    }
}