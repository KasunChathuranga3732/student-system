import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CountService {
  rowCount:number = 0;

  constructor() { }

  setRowCount(count:number){
    this.rowCount = count;
  }

  getRowCount(){
    return this.rowCount;
  }
}
