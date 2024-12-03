import {calculateNumber} from './0-calcul.js';
import assert from 'assert';

it('calculateNumber', () => {
  assert.equal(calculateNumber(1, 3), 4);
  assert.equal(calculateNumber(1, 3.7), 5);
  assert.equal(calculateNumber(1.2, 3.7), 5);
  assert.equal(calculateNumber(1.5, 3.7), 6);
});
