/* eslint-disable */

const { expect } = require('chai');
const sinon = require('sinon');

const utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { spy } = require('sinon');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber', () => {
    const stub = sinon.stub(utils, 'calculateNumber');
    stub.returns(10);

    const spy = sinon.spy(console, 'log');

    const apiRequestRes = sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true); // stub of calculateNumber(100, 20){return 10} == sendPaymentRequestToApi(100, 20)
    expect(spy.calledOnceWithExactly('The total is: 10'));
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(10);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequestRes); // calculateNumber() == sendPaymentRequestToApi() == 10 (calculateNumber changed behavior)

    stub.restore();
    spy.restore();
  });
});