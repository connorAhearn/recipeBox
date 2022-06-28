import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RecipeSubmitService {

  api_url: string = "http://localhost:5000/";

  constructor(private http: HttpClient) { }

  getRecipe(recipe: string) {
    return this.http.get(this.api_url, {responseType: 'text'})
  }
}
