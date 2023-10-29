import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {CountService} from "../count.service";

@Component({
  selector: 'app-tables',
  templateUrl: './tables.component.html',
  styleUrls: ['./tables.component.scss']
})
export class TablesComponent implements OnInit{
  schoolList:any
  classList:any
  assessmentAreaList:any
  answerList:any
  correctAnswerList:any
  categoryList:any
  awardList:any
  subjectList:any
  studentList:any
  summaryList:string[][] = []
  pageNumber:number = 1
  flag:boolean = true
  pageMax:number = 1;
  Object = Object;


  constructor(private http:HttpClient, private count:CountService) {
  }

  ngOnInit() {
    this.setPageMax();
    this.getSchoolList();
    this.getClassList();
    this.getAssessmentAreaList();
    this.getAnswerList();
    this.getCorrectAnswerList();
    this.getCategoryList();
    this.getAwardList();
    this.getSubjectList();
    this.getStudentList();
    this.getStudentList();
    setTimeout(()=>this.getSummaryList(), 2000);

  }

  setPageMax(){
    let rowCount = this.count.getRowCount();
    if(rowCount % 5000 == 0){
      this.pageMax = rowCount/5000;
    } else {
      this.pageMax = rowCount/5000 + 1;
    }
    console.log(this.pageMax);
  }

  getSchoolList(){
    this.http.get('http://127.0.0.1:8000/schools/')
      .subscribe(response => {
          this.schoolList = response;
        })
  }

  getClassList(){
    this.http.get('http://127.0.0.1:8000/classes/')
      .subscribe(response => {
        this.classList = response;
        console.log(response)
      })
  }

  getAssessmentAreaList(){
    this.http.get('http://127.0.0.1:8000/assess-areas/')
      .subscribe(response => {
        this.assessmentAreaList = response;
      })
  }

  getAnswerList(){
    this.http.get('http://127.0.0.1:8000/answers/')
      .subscribe(response => {
        this.answerList = response;
      })
  }

  getCorrectAnswerList(){
    this.http.get('http://127.0.0.1:8000/cor-answers/')
      .subscribe(response => {
        this.correctAnswerList = response;
      })
  }

  getCategoryList(){
    this.http.get('http://127.0.0.1:8000/categories/')
      .subscribe(response => {
        this.categoryList = response;
      })
  }

  getAwardList(){
    this.http.get('http://127.0.0.1:8000/awards/')
      .subscribe(response => {
        this.awardList = response;
      })
  }

  getSubjectList(){
    this.http.get('http://127.0.0.1:8000/subjects/')
      .subscribe(response => {
        this.subjectList = response;
      })
  }

  getStudentList(){
    this.http.get('http://127.0.0.1:8000/students/')
      .subscribe(response => {
        this.studentList = response;
      })
  }

  getSummaryList(){
    this.flag = false;
    this.http.get<any>(`http://127.0.0.1:8000/summary/${this.pageNumber}`)
      .subscribe(response => {
        this.summaryList = response;
        this.flag = true;
      })
  }

  pageNumberDecrement() {
    this.pageNumber -= 1;
    this.getSummaryList();
  }

  pageNumberIncrement() {
    this.pageNumber += 1;
    this.getSummaryList();
  }
}
