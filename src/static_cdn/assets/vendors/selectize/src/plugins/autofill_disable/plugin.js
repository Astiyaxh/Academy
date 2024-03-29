/**
 * Plugin: "autofill_disable" (selectize)
 * Copyright (c) 2013 Brian Reavis & contributors
 * Copyright (c) 2020 Selectize Team & contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
 * file except in compliance with the License. You may obtain a copy of the License at:
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 * ANY KIND, either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 *
 * @author Ris Adams <selectize@risadams.com>
 */

Selectize.define("autofill_disable", function (options) {
  var self = this;

  self.setup = (function () {
    var original = self.setup;
    return function () {
      original.apply(self, arguments);

      // https://stackoverflow.com/questions/30053167/autocomplete-off-vs-false
      self.$control_input.attr({ autocomplete: "new-password", autofill: "no" });
    };
  })();
});
