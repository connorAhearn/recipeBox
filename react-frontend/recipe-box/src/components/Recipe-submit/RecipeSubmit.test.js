import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import RecipeSubmit from './RecipeSubmit';

describe('<RecipeSubmit />', () => {
  test('it should mount', () => {
    render(<RecipeSubmit />);
    
    const recipeSubmit = screen.getByTestId('RecipeSubmit');

    expect(recipeSubmit).toBeInTheDocument();
  });
});