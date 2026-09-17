/**
 * TOK — "You Have a Frame" (Nacirema) — class entries + guessing game
 *
 * Bound sheet: TOK — You Have a Frame — Nacirema Submissions
 * https://docs.google.com/spreadsheets/d/1AA506-60kvbzZgaAUSVrQ614EFsi7GnduJ_5Lb3_Qtc/edit
 *
 * Two tabs, created automatically on first use:
 *   Entries  — timestamp | id | name | class | paragraph | answer
 *   Guesses  — timestamp | entry_id | guesser | class | guess
 *
 * The older "Submissions" tab from the first version is no longer used and can be deleted.
 *
 * DEPLOY (once):
 *   Sign in as the account that owns the sheet.
 *   Deploy ▸ New deployment ▸ type: Web app
 *   Execute as:      Me
 *   Who has access:  Anyone
 *
 *   ⚠  It must be the literal "Anyone" option — NOT "Anyone with a Google Account".
 *      A fetch() from the lesson page carries no Google sign-in, so any setting that
 *      requires one returns Google's "You need access" page instead of JSON, and the
 *      whole class fails, not just some of them. Symptom to recognise: opening the
 *      /exec URL in a browser shows a Drive "You need access" screen.
 *
 *   Deploy ▸ Authorize ▸ copy the /exec URL.
 *   Paste that URL into APPS_SCRIPT_URL near the top of the lesson page's <script>.
 *
 * CHANGING THE DEPLOYMENT LATER:
 *   Deploy ▸ Manage deployments ▸ pencil icon on the active deployment ▸ change ▸ Deploy.
 *   Editing an existing deployment keeps the same /exec URL. Creating a NEW deployment
 *   issues a new URL, which then has to be pasted into the lesson page again. A URL that
 *   returns "You need access" is dead — settings changed elsewhere will not revive it.
 */

var SHEET_ID = '1AA506-60kvbzZgaAUSVrQ614EFsi7GnduJ_5Lb3_Qtc';

var ENTRY_TAB    = 'Entries';
var ENTRY_HEAD   = ['timestamp', 'id', 'name', 'class', 'paragraph', 'answer'];
var GUESS_TAB    = 'Guesses';
var GUESS_HEAD   = ['timestamp', 'entry_id', 'guesser', 'class', 'guess'];

function tab_(name, headers, wideCol) {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheetByName(name);
  if (!sh) sh = ss.insertSheet(name);
  if (sh.getLastRow() === 0) {
    sh.appendRow(headers);
    sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    sh.setFrozenRows(1);
    if (wideCol) sh.setColumnWidth(wideCol, 520);
  }
  return sh;
}

function entriesTab_() { return tab_(ENTRY_TAB, ENTRY_HEAD, 5); }
function guessesTab_() { return tab_(GUESS_TAB, GUESS_HEAD, 5); }

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function s_(v, n) { return String(v === null || v === undefined ? '' : v).slice(0, n); }

function doPost(e) {
  try {
    var b = JSON.parse(e.postData.contents);

    if (b.action === 'submit') {
      entriesTab_().appendRow([
        b.timestamp || new Date().toISOString(),
        s_(b.id, 40),
        s_(b.name || 'anonymous', 60),
        s_(b.klass, 40),
        s_(b.paragraph, 2000),
        s_(b.answer, 200)
      ]);
      return json_({ ok: true });
    }

    if (b.action === 'guess') {
      guessesTab_().appendRow([
        b.timestamp || new Date().toISOString(),
        s_(b.entryId, 40),
        s_(b.guesser || 'anonymous', 60),
        s_(b.klass, 40),
        s_(b.guess, 200)
      ]);
      return json_({ ok: true });
    }

    return json_({ error: 'unknown action' });
  } catch (err) {
    return json_({ error: String(err) });
  }
}

function rows_(sh, headers) {
  var last = sh.getLastRow();
  if (last < 2) return [];
  return sh.getRange(2, 1, last - 1, headers.length).getValues();
}

function doGet(e) {
  try {
    var p      = (e && e.parameter) || {};
    var action = p.action || 'getAll';
    if (action !== 'getAll') return json_({ error: 'unknown action' });

    var wanted = p.klass || '';

    var entries = [];
    rows_(entriesTab_(), ENTRY_HEAD).forEach(function (r) {
      if (!r[4]) return;
      if (wanted && String(r[3]) !== wanted) return;
      entries.push({
        timestamp: r[0], id: String(r[1]), name: r[2],
        klass: r[3], paragraph: r[4], answer: r[5]
      });
    });

    var guesses = [];
    rows_(guessesTab_(), GUESS_HEAD).forEach(function (r) {
      if (!r[4]) return;
      if (wanted && String(r[3]) !== wanted) return;
      guesses.push({
        timestamp: r[0], entryId: String(r[1]),
        guesser: r[2], klass: r[3], guess: r[4]
      });
    });

    return json_({ entries: entries, guesses: guesses });
  } catch (err) {
    return json_({ error: String(err) });
  }
}

/** Run once from the editor to create both tabs before class. */
function setup() {
  entriesTab_();
  guessesTab_();
  Logger.log('Ready: ' + SpreadsheetApp.openById(SHEET_ID).getUrl());
}
