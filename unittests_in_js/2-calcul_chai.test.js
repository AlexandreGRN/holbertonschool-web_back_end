/* eslint-disable */

const { expect } = require('chai');
const calculateNumber = require('./1-calcul');

describe('when type is SUM', function () {
    it('when type is SUM', function () {
        expect(calculateNumber('SUM', 1, 1)).to.equal(2);
    });
});  

describe('when type is SUBTRACT', function () {
    it('when type is SUBTRACT', function () {
        expect(calculateNumber('SUBTRACT', 1.3, 1)).to.equal(0);
    });
});  

describe('when type is DIVIDE', () => {
    it('it round the first argument', () => {
        expect(calculateNumber('DIVIDE', 10.0, 2)).to.equal(5);
    });

    it('it should return Error if b is equal to 0', () => {
        expect(calculateNumber('DIVIDE', 10.3, 0)).to.equal('Error');
    });
});
