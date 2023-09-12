#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOfoccur = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      numOfoccur += 1;
    }
  }
  return (numOfoccur);
};
