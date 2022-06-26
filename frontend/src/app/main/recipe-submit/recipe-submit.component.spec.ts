import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecipeSubmitComponent } from './recipe-submit.component';

describe('RecipeSubmitComponent', () => {
  let component: RecipeSubmitComponent;
  let fixture: ComponentFixture<RecipeSubmitComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RecipeSubmitComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecipeSubmitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
