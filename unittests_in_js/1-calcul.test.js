/* eslint-disable */

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('when type is SUM', function () {
    it('when type is SUM', function () {
        assert.equal(calculateNumber('SUM', 1, 1), 2);
    });
});  

describe('when type is SUBTRACT', function () {
    it('when type is SUBTRACT', function () {
        assert.equal(calculateNumber('SUBTRACT', 1.3, 1), 0);
    });
});  

describe('when type is DIVIDE', () => {
    it('it round the first argument', () => {
        assert.equal(calculateNumber('DIVIDE', 10.0, 2), 5);
    });

    it('it should return Error if b is equal to 0', () => {
        assert.equal(calculateNumber('DIVIDE', 10.3, 0), 'Error');
    });
  });
