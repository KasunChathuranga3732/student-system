import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { TablesComponent } from './tables/tables.component';
import {RouterModule, Routes} from "@angular/router";
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import { HomeComponent } from './home/home.component';


const route:Routes = [
  {path: '', redirectTo:'/home', pathMatch:'full'},
  {
    path:'home',
    component:HomeComponent
  },
  {
    path:'tables',
    component:TablesComponent
  }
]

@NgModule({
  declarations: [
    AppComponent,
    TablesComponent,
    HomeComponent
  ],
    imports: [
        BrowserModule,
        RouterModule.forRoot(route),
        HttpClientModule,
        FormsModule,
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
