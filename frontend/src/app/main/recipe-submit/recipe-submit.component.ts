import { Component, OnInit } from '@angular/core';
import { RecipeSubmitService } from './recipe-submit.service'

@Component({
  selector: 'app-recipe-submit',
  templateUrl: './recipe-submit.component.html',
  styleUrls: ['./recipe-submit.component.sass']
})
export class RecipeSubmitComponent implements OnInit {

  constructor(private recipeSubmitService: RecipeSubmitService) { }

  ngOnInit(): void {
  }

  submit(recipe:string) {
    this.recipeSubmitService.getRecipe(recipe)
      .subscribe({
        next: data => console.log(data),
        error: error => console.log(error)
      })
  }

}
