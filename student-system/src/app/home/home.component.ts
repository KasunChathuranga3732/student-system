import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {CountService} from "../count.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  uploaded:boolean = false
  fileSelect:boolean = false
  formData = new FormData();

  constructor(private http: HttpClient, private count:CountService) {}

  onFileSelected(event: any) {
    this.fileSelect = true;
    const file: File = event.target.files[0];
    this.formData.append('csvFile', file);
  }

  uploadFile() {
    this.http.post<number>('http://127.0.0.1:8000/read/', this.formData)
      .subscribe(
        (response) => {
          this.uploaded = true;
          this.count.setRowCount(response);
        },
        (error) => {
          alert("Upload Failed")
        }
      );
  }
}
