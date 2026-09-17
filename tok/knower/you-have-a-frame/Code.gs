/**
 * TOK — "You Have a Frame" (Nacirema) — class submissions backend
 *
 * Bound sheet: TOK — You Have a Frame — Nacirema Submissions
 * https://docs.google.com/spreadsheets/d/1AA506-60kvbzZgaAUSVrQ614EFsi7GnduJ_5Lb3_Qtc/edit
 *
 * DEPLOY (once):
 *   Deploy ▸ New deployment ▸ type: Web app
 *   Execute as: Me
 *   Who has access: Anyone
 *   Deploy ▸ Authorize ▸ copy the /exec URL
 *   Paste that URL into APPS_SCRIPT_URL at the top of the lesson page's <script>.
 */

var SHEET_ID  = '1AA506-60kvbzZgaAUSVrQ614EFsi7GnduJ_5Lb3_Qtc';
var TAB_NAME  = 'Submissions';
var HEADERS   = ['timestamp', 'name', 'class', 'paragraph', 'answer'];

function sheet_() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheetByName(TAB_NAME);
  if (!sh) {
    sh = ss.getSheets()[0];
    sh.setName(TAB_NAME);
  }
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
    sh.setFrozenRows(1);
    sh.setColumnWidth(4, 520);
  }
  return sh;
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  try {
    var body = JSON.parse(e.postData.contents);
    if (body.action !== 'submit') return json_({ error: 'unknown action' });

    sheet_().appendRow([
      body.timestamp || new Date().toISOString(),
      String(body.name || 'anonymous').slice(0, 60),
      String(body.klass || '').slice(0, 40),
      String(body.paragraph || '').slice(0, 2000),
      String(body.answer || '').slice(0, 200)
    ]);
    return json_({ ok: true });
  } catch (err) {
    return json_({ error: String(err) });
  }
}

function doGet(e) {
  try {
    var action = (e && e.parameter && e.parameter.action) || 'getAll';
    if (action !== 'getAll') return json_({ error: 'unknown action' });

    var wanted = (e && e.parameter && e.parameter.klass) || '';
    var sh = sheet_();
    var last = sh.getLastRow();
    if (last < 2) return json_([]);

    var rows = sh.getRange(2, 1, last - 1, HEADERS.length).getValues();
    var out = [];
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      if (!r[3]) continue;
      if (wanted && String(r[2]) !== wanted) continue;
      out.push({
        timestamp: r[0],
        name:      r[1],
        klass:     r[2],
        paragraph: r[3],
        answer:    r[4]
      });
    }
    return json_(out);
  } catch (err) {
    return json_({ error: String(err) });
  }
}

/** Run once from the editor to create the tab and headers before class. */
function setup() {
  sheet_();
  Logger.log('Ready: ' + SpreadsheetApp.openById(SHEET_ID).getUrl());
}
